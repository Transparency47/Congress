# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1104?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1104
- Title: WATCH Act
- Congress: 119
- Bill type: S
- Bill number: 1104
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2026-04-20T19:22:30Z
- Update date including text: 2026-04-20T19:22:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1104",
    "number": "1104",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "WATCH Act",
    "type": "S",
    "updateDate": "2026-04-20T19:22:30Z",
    "updateDateIncludingText": "2026-04-20T19:22:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T15:35:46Z",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "OR"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "NE"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "FL"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MI"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1104is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1104\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Schmitt (for himself, Mr. Merkley , Mr. Ricketts , Mr. Fetterman , Mr. Scott of Florida , Mr. Peters , and Ms. Ernst ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend section 495 of the Public Health Service Act to require inspections of foreign laboratories conducting biomedical and behavioral research to ensure compliance with applicable animal welfare requirements, and for other purposes\n#### 1. Short titles\nThis Act may be cited as the Worldwide Animal Testing Compliance and Harmonization Act of 2025 or the WATCH Act .\n#### 2. Foreign laboratory inspections and certification\n##### (a) In general\nSection 495 of the Public Health Service Act ( 42 U.S.C. 289d ) is amended by adding at the end the following:\n(f) Inspection and certification of foreign laboratories (1) In general As a condition of eligibility to perform research involving animals under a grant, contract, or cooperative agreement administered by the National Institutes of Health or any national research institute, a laboratory located outside the United States that receives Federal funds shall be subject to quarterly inspections to evaluate compliance with the requirements under this title. (2) Inspection and certification requirements (A) Quarterly inspection process The Secretary, in consultation with appropriate foreign regulatory authorities and international organizations, shall establish and implement a process for conducting quarterly inspections of foreign laboratories that have received an Animal Welfare Assurance (as defined in section 9.2 of title 42, Code of Federal Regulations) to ensure their continued compliance with the requirements under this title. (B) Assurances The inspection process established by the Secretary pursuant to subparagraph (A) shall evaluate the compliance of foreign laboratories with the requirements under subsection (c)(1), including\u2014 (i) the establishment and operation of animal care committees; (ii) the review and evaluation of animal care and treatment; and (iii) proper record-keeping and reporting procedures. (3) Certification of compliance and public access (A) Issuance Following each quarterly inspection required under paragraph (2)(A), the inspecting authority shall issue a certification of compliance to the laboratories determined to be in compliance with the requirements under paragraph (2)(B). (B) Public access Copies of the certificates of compliance issued pursuant to subparagraph (A) shall be maintained by the Office of Laboratory Animal Welfare and shall remain publicly accessible with other information about currently issued Animal Welfare Assurances. (C) Corrective action Laboratories that fail to comply with the requirements under paragraph (2)(B) shall be given a reasonable opportunity to take corrective action. (4) Suspension or revocation of grant or contract for non-compliant foreign laboratories If the Secretary determines that a foreign facility is not in compliance with the requirements under subsection (c)(1) and does not take appropriate corrective action after given a reasonable opportunity to do so, the Secretary shall suspend or revoke the applicable grant, contract, or cooperative agreement involving research on animals under such conditions as the Director of NIH determines appropriate, in accordance with subsection (d). (5) Designation of inspecting authority The Secretary, in consultation with the Director of NIH, shall designate an appropriate authority to conduct the quarterly inspections required under paragraph (2)(A) and issue certifications of compliance in accordance with paragraph (3). (6) Coordination with foreign authorities The Secretary and the Director of NIH shall coordinate with appropriate foreign regulatory authorities and enter into agreements with foreign governments, as needed, to facilitate the implementation and enforcement of this subsection, while respecting the sovereignty and laws of foreign nations. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2026-01-20",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "7165",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "WATCH Act",
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
        "updateDate": "2025-04-06T11:36:19Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1104is.xml"
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
      "title": "WATCH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "WATCH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Worldwide Animal Testing Compliance and Harmonization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 495 of the Public Health Service Act to require inspections of foreign laboratories conducting biomedical and behavioral research to ensure compliance with applicable animal welfare requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T04:18:15Z"
    }
  ]
}
```
