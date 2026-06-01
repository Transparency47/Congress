# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3604?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3604
- Title: Public Health Nursing Act
- Congress: 119
- Bill type: S
- Bill number: 3604
- Origin chamber: Senate
- Introduced date: 2026-01-08
- Update date: 2026-02-04T15:21:49Z
- Update date including text: 2026-02-04T15:21:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in Senate
- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-01-08: Introduced in Senate

## Actions

- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3604",
    "number": "3604",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Public Health Nursing Act",
    "type": "S",
    "updateDate": "2026-02-04T15:21:49Z",
    "updateDateIncludingText": "2026-02-04T15:21:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-08",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-01-08T19:00:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "IL"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "OR"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3604is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3604\nIN THE SENATE OF THE UNITED STATES\nJanuary 8 (legislative day, January 7), 2026 Mr. Markey (for himself, Ms. Duckworth , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to require the Secretary of Health and Human Services to carry out activities to establish, expand, and sustain a public health nursing workforce, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Health Nursing Act .\n#### 2. Public health nursing workforce\nPart E of title VII of the Public Health Service Act ( 42 U.S.C. 294n et seq. ) is amended by adding at the end the following:\n4 Public health nursing workforce 780. Public health nursing workforce (a) In general The Secretary shall carry out activities relating to establishing, expanding, and sustaining a public health nursing workforce, including by making grants to State, local, and territorial public health departments. (b) Use of funds for public health departments (1) In general The recipient of a grant under subsection (a) shall use the grant funds for the following: (A) Costs (including wages and benefits) relating to the recruiting, hiring, and training of licensed registered nurses to serve as public health nurses\u2014 (i) who are employed by the State, territorial, or local public health department involved, particularly in medically underserved areas; and (ii) who work in public health facilities, including mobile health clinics and acute care hospitals, or who provide home visitation. (B) Costs of medical supplies, including personal protective equipment, necessary to carry out the activities described in subparagraph (A). (C) Administrative costs and activities relating to grant activities. (2) Subgrants The recipient of a grant under subsection (a) may make subgrants to local health departments to be used for the activities described in paragraph (1). (c) Priority In selecting recipients of grants under subsection (a), the Secretary shall give priority to applicants that\u2014 (1) propose to serve\u2014 (A) areas with populations that have a high rate of chronic disease, infant mortality, or maternal morbidity and mortality; (B) low-income populations, including medically underserved populations (as defined in section 330(b)); (C) populations residing in health professional shortage areas (as defined in section 332(a)); (D) populations residing in maternity care health professional target areas identified under section 332(k); or (E) rural or traditionally underserved populations; (2) demonstrate a plan for providing services, to the maximum extent practicable, in the language and cultural context more appropriate to individuals expected to be served by the program; and (3) have a documented collective bargaining agreement with 1 or more labor organizations representing employees of the applicant or have an explicit policy not to interfere with the rights of employees of the applicant under section 7 of the National Labor Relations Act. (d) Maintenance of effort The recipient of a grant under subsection (a) shall agree to maintain expenditures of non-Federal amounts for activities described in subsection (b) at a level that is not less than the level of such expenditures maintained by the recipient for the fiscal year preceding the fiscal year for which the recipient receives such a grant. (e) Public health nurse defined In this section, the term public health nurse means a nurse providing health care services and education regarding preventive health, nutrition, infectious diseases, chronic disease management, and maternal health, prenatal, and postpartum care in order to improve maternal and infant health outcomes. (f) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $5,000,000,000 for each of fiscal years 2026 through 2035. .",
      "versionDate": "2026-01-08",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-08",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6989",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Public Health Nursing Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-02-04T15:21:49Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3604is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to require the Secretary of Health and Human Services to carry out activities to establish, expand, and sustain a public health nursing workforce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:48Z"
    },
    {
      "title": "Public Health Nursing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T10:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Public Health Nursing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    }
  ]
}
```
