# Secure File Intake Plan v1

**Purpose:** Define the simplest credible approach for receiving customer financial files during the first design partner pilot, with appropriate security controls for handling sensitive GL and budget data.

**Alignment:** Stage 1 of `ops/live_pilot_workflow_v1.md`, DEC-009 (trust and auditability), Priority 1.5 in `ops/pilot_gaps_and_build_priorities_v1.md`

---

## Recommended Approach: Google Drive with Per-Customer Folders

For the first 1–2 design partners, use a dedicated Google Workspace shared folder structure with restricted access.

### Why this is appropriate for the pilot

1. **Immediate availability** — no custom development required. Go-live in hours.
2. **Familiar to customers** — every finance team knows Google Drive. No onboarding friction.
3. **Access controls** — Google Workspace supports folder-level permissions, audit logs, and 2FA enforcement.
4. **File versioning** — Google Drive tracks upload history and file versions automatically.
5. **Encrypted at rest and in transit** — Google Workspace encrypts data by default (AES-256 at rest, TLS in transit).
6. **Sufficient for pilot scale** — supports 1–3 customers with manual folder management.

### Why this is not a long-term solution

- No automated processing pipeline (files must be manually downloaded for validation)
- No custom upload confirmation or validation feedback
- Folder management is manual and does not scale beyond a handful of customers
- No integration with the validation or computation scripts
- Access audit logs require manual review via Google Admin Console

---

## Folder Structure

```
E-Solutions Pilot Data/
├── {customer_name}/
│   ├── uploads/
│   │   ├── 2026-02/
│   │   │   ├── gl_export_2026-02.csv
│   │   │   └── budget_2026.csv
│   │   └── 2026-03/
│   │       ├── gl_export_2026-03.csv
│   │       └── budget_2026.csv (if revised)
│   ├── coa/
│   │   └── coa_mapping_v1.csv
│   └── deliverables/
│       ├── variance_memo_2026-02_DRAFT.pdf
│       └── variance_memo_2026-02_FINAL.pdf
└── {next_customer}/
    └── ...
```

---

## Access Controls

| Role | Access level | Scope |
|------|-------------|-------|
| Customer Controller | Edit access to their `uploads/` folder only | Cannot see other customers or `deliverables/` until memo is ready for review |
| E-Solutions Operator | Full access to all customer folders | Manages file processing and delivery |
| Finance QA Reviewer | Read access to specific customer folders (granted per cycle) | Reviews draft memos only — no access to raw GL data unless needed |

### Rules

1. **No cross-customer access.** Each customer folder is shared only with that customer's designated contacts and E-Solutions operators. No customer can see another customer's folder.
2. **2FA required.** All Google accounts with access to the pilot data folder must have 2-factor authentication enabled.
3. **Share by email invitation only.** No public links, no "anyone with the link" sharing.
4. **Operator reviews access list monthly.** At each cycle, verify that only authorized accounts have access.

---

## File Handling Steps

### When the customer uploads files:

1. **Notification:** Operator receives an email notification from Google Drive that a new file was added.
2. **Download:** Operator downloads the file(s) to a local working directory for processing.
3. **Log the upload:** Record in the cycle tracking spreadsheet: customer name, file name, upload timestamp, file hash (computed locally).
4. **Run validation:** Execute `python product/validation_checks_v1.py <file_path> --period YYYY-MM`.
5. **If validation passes:** Proceed to COA mapping and variance computation.
6. **If validation fails:** Notify the customer with the specific error(s) and request a corrected re-upload.
7. **Archive:** After the cycle is complete, move processed files to a `processed/` subfolder within the customer's upload directory.

### After memo is approved:

1. Upload the final PDF to the customer's `deliverables/` folder.
2. Send an email notification with a link to the file.
3. Log the delivery in the cycle tracking spreadsheet.

---

## Retention and Deletion

| Data type | Retention | Deletion |
|-----------|-----------|----------|
| Raw GL and budget files | Duration of pilot + 90 days | Deleted from Google Drive and local copies after retention period |
| COA mapping | Duration of pilot + 90 days | Retained unless customer requests earlier deletion |
| Draft memos | Deleted after final memo is approved | Operator deletes manually |
| Final delivered memos | Duration of pilot + 12 months | Customer retains their copy; E-Solutions copy deleted after retention |
| Local processing copies | Deleted after each cycle is complete | Operator deletes from local machine |

### Customer-initiated deletion

The customer can request deletion of all their data at any time. Upon request:
1. Delete the customer's entire Google Drive folder
2. Delete all local copies of their data
3. Confirm deletion in writing to the customer within 5 business days

---

## Operator Responsibilities

| Responsibility | Frequency |
|----------------|-----------|
| Check for new uploads | Daily during active cycles |
| Download and validate files | Within 4 hours of upload notification |
| Notify customer of validation results | Within 4 hours of validation |
| Review folder access permissions | Monthly |
| Delete local processing copies | After each cycle |
| Apply retention/deletion policy | Quarterly |
| Maintain upload log (spreadsheet) | Every upload |

---

## Manual vs. Automated (Current vs. Target)

| Step | Current (pilot) | Target (post-pilot) |
|------|-----------------|---------------------|
| File upload | Customer uploads to Google Drive | Self-service portal with drag-and-drop |
| Upload notification | Google Drive email notification | Automated webhook + Slack notification |
| File download | Manual by operator | Automated pipeline pulls from upload |
| Validation | Operator runs script manually | Auto-triggered on upload |
| Validation feedback | Operator emails customer | Portal shows validation status in real time |
| Delivery | Operator uploads PDF to Drive | Automated portal delivery + encrypted email |
| Access management | Manual Google Drive sharing | Role-based access control in portal |
| Audit log | Spreadsheet + Google Drive history | Automated audit trail in application |

---

## Alternative Approaches Considered

| Option | Why not chosen for pilot |
|--------|--------------------------|
| Custom web portal | Requires development time (1–2 weeks minimum). Not justified for 1–2 customers. Build for post-pilot. |
| Dropbox Business | Equivalent to Google Drive but adds a tool the team may not already use. |
| SFTP server | Secure but poor UX for non-technical finance teams. |
| Email with attachments | No file isolation, no access controls, attachment size limits, no audit trail. Unacceptable. |
| S3 pre-signed upload URLs | Good for automation but requires customer to use a custom link flow. Save for portal integration. |

---

## Security Checklist Before First Upload

- [ ] Google Workspace account has 2FA enabled for all operators
- [ ] Customer folder created with restricted sharing (email invitation only)
- [ ] Customer contacts verified and added with correct access level
- [ ] No public links or "anyone with the link" sharing enabled
- [ ] Upload log spreadsheet created
- [ ] Retention policy communicated to customer (verbally or in DPA)
- [ ] Local processing directory created with appropriate file permissions

---

**This plan is designed for the pilot phase only. A purpose-built upload portal with automated validation and delivery is planned for post-pilot development.**
