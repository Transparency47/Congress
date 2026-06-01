# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4357?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4357
- Title: Hazard Pay for Health Care Heroes Act
- Congress: 119
- Bill type: S
- Bill number: 4357
- Origin chamber: Senate
- Introduced date: 2026-04-21
- Update date: 2026-05-13T19:20:17Z
- Update date including text: 2026-05-13T19:20:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in Senate
- 2026-04-21 - IntroReferral: Introduced in Senate
- 2026-04-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-21: Introduced in Senate

## Actions

- 2026-04-21 - IntroReferral: Introduced in Senate
- 2026-04-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4357",
    "number": "4357",
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
    "title": "Hazard Pay for Health Care Heroes Act",
    "type": "S",
    "updateDate": "2026-05-13T19:20:17Z",
    "updateDateIncludingText": "2026-05-13T19:20:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-21",
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
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T19:17:34Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4357is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4357\nIN THE SENATE OF THE UNITED STATES\nApril 21, 2026 Mr. Markey introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to provide for emergency grants to safeguard essential health care workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hazard Pay for Health Care Heroes Act .\n#### 2. Safeguarding essential health care workers\nThe Public Health Service Act is amended by inserting after section 319D\u20131 ( 42 U.S.C. 247d\u20134b ) the following:\n319D\u20132. Emergency grants to safeguard essential health care workers (a) Definitions In this section: (1) Emergency or disaster The term emergency or disaster means\u2014 (A) a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act; (B) an emergency declared by the President under section 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act; (C) a national emergency declared by the President under the National Emergencies Act; (D) a public health emergency declared under section 319; and (E) a State, local, territorial, or Tribal emergency or disaster, as declared by the applicable State, local, territorial, or Tribal government. (2) Eligible health care worker The term eligible health care worker means an essential health care worker whose work cannot be conducted remotely. (3) Essential health care worker The term essential health care worker means\u2014 (A) a health care provider, including a direct care worker (as defined in section 799B); (B) a medical technologist; (C) a public health worker; (D) an orderly (as defined in the 2010 Standard Occupational Classifications of the Department of Labor under the code for Orderlies (31\u20131015)); (E) an environmental service, janitorial, or custodial worker in a health care setting; and (F) any other professional role that the Secretary determines is essential to the care of patients or the maintenance of public health. (b) Grants (1) In general The Secretary may make grants to public or private nonprofit health care facilities and home health agencies for use in accordance with paragraph (2). (2) Use of funds (A) Hazardous duty compensation (i) In general The recipient of a grant under paragraph (1) shall use the grant funds to provide hazardous duty compensation to eligible health care workers for work performed during the period of an emergency or disaster in cases in which the Secretary determines that\u2014 (I) the performance of the work by the eligible health care worker for the applicable health care facility or home health agency is hazardous; or (II) the commute of the eligible health care worker is hazardous. (ii) Requirement (I) In general Subject to subclause (II), the amount of hazardous duty compensation under clause (i) shall be not more than $13 per hour, which shall be in addition to the wages or remuneration the eligible health care worker otherwise receives for the work. (II) Maximum amount The total amount of hazardous duty compensation received by any 1 eligible health care worker under this subparagraph may not exceed $25,000 per year. (B) Additional uses The recipient of a grant under paragraph (1) may use the grant funds to provide safety measures to safeguard and protect eligible health care workers from hazards due to the applicable emergency or disaster, including alternative transit options, personal protective equipment, and other safety measures. (c) Authorization of appropriations There are authorized to be appropriated to carry out this section such sums as may be necessary. .",
      "versionDate": "2026-04-21",
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
        "actionDate": "2026-04-23",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "8484",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Hazard Pay for Health Care Heroes Act",
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
        "updateDate": "2026-05-13T19:13:52Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4357is.xml"
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
      "title": "Hazard Pay for Health Care Heroes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Hazard Pay for Health Care Heroes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to provide for emergency grants to safeguard essential health care workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:33Z"
    }
  ]
}
```
