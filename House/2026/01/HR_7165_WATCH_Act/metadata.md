# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7165?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7165
- Title: WATCH Act
- Congress: 119
- Bill type: HR
- Bill number: 7165
- Origin chamber: House
- Introduced date: 2026-01-20
- Update date: 2026-04-20T19:22:37Z
- Update date including text: 2026-04-20T19:22:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-20: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-20: Introduced in House

## Actions

- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-20",
    "latestAction": {
      "actionDate": "2026-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7165",
    "number": "7165",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "WATCH Act",
    "type": "HR",
    "updateDate": "2026-04-20T19:22:37Z",
    "updateDateIncludingText": "2026-04-20T19:22:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-20",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-01-20T17:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "NV"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7165ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7165\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2026 Mr. Steube (for himself and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend section 495 of the Public Health Service Act to require inspections of foreign laboratories conducting biomedical and behavioral research to ensure compliance with applicable animal welfare requirements, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Worldwide Animal Testing Compliance and Harmonization Act of 2026 or the WATCH Act .\n#### 2. Foreign laboratory inspections and certification\n##### (a) In general\nSection 495 of the Public Health Service Act ( 42 U.S.C. 289d ) is amended by adding at the end the following:\n(f) Inspection and certification of foreign laboratories (1) In general As a condition of eligibility to perform research involving animals under a grant, contract, or cooperative agreement administered by the National Institutes of Health or any national research institute, a laboratory located outside the United States that receives Federal funds shall be subject to quarterly inspections to evaluate compliance with the requirements under this title. (2) Inspection and certification requirements (A) Quarterly inspection process The Secretary, in consultation with appropriate foreign regulatory authorities and international organizations, shall establish and implement a process for conducting quarterly inspections of foreign laboratories that have received an Animal Welfare Assurance (as defined in section 9.2 of title 42, Code of Federal Regulations) to ensure their continued compliance with the requirements under this title. (B) Assurances The inspection process established by the Secretary pursuant to subparagraph (A) shall evaluate the compliance of foreign laboratories with the requirements under subsection (c)(1), including\u2014 (i) the establishment and operation of animal care committees; (ii) the review and evaluation of animal care and treatment; and (iii) proper record-keeping and reporting procedures. (3) Certification of compliance and public access (A) Issuance Following each quarterly inspection required under paragraph (2)(A), the inspecting authority shall issue a certification of compliance to the laboratories determined to be in compliance with the requirements under paragraph (2)(B). (B) Public access Copies of the certificates of compliance issued pursuant to subparagraph (A) shall be maintained by the Office of Laboratory Animal Welfare and shall remain publicly accessible with other information about currently issued Animal Welfare Assurances. (C) Corrective action Laboratories that fail to comply with the requirements under paragraph (2)(B) shall be given a reasonable opportunity to take corrective action. (4) Suspension or revocation of grant or contract for non-compliant foreign laboratories If the Secretary determines that a foreign facility is not in compliance with the requirements under subsection (c)(1) and does not take appropriate corrective action after given a reasonable opportunity to do so, the Secretary shall suspend or revoke the applicable grant, contract, or cooperative agreement involving research on animals under such conditions as the Director of NIH determines appropriate, in accordance with subsection (d). (5) Designation of inspecting authority The Secretary, in consultation with the Director of NIH, shall designate an appropriate authority to conduct the quarterly inspections required under paragraph (2)(A) and issue certifications of compliance in accordance with paragraph (3). (6) Coordination with foreign authorities The Secretary and the Director of NIH shall coordinate with appropriate foreign regulatory authorities and enter into agreements with foreign governments, as needed, to facilitate the implementation and enforcement of this subsection, while respecting the sovereignty and laws of foreign nations. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2026-01-20",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-25",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1104",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "WATCH Act",
      "type": "S"
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
        "updateDate": "2026-04-20T19:22:36Z"
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
      "date": "2026-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7165ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "WATCH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T06:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WATCH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-15T06:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Worldwide Animal Testing Compliance and Harmonization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-15T06:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 495 of the Public Health Service Act to require inspections of foreign laboratories conducting biomedical and behavioral research to ensure compliance with applicable animal welfare requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-15T06:18:27Z"
    }
  ]
}
```
