# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8484?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8484
- Title: Hazard Pay for Health Care Heroes Act
- Congress: 119
- Bill type: HR
- Bill number: 8484
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-13T19:24:49Z
- Update date including text: 2026-05-13T19:24:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8484",
    "number": "8484",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000602",
        "district": "12",
        "firstName": "Summer",
        "fullName": "Rep. Lee, Summer L. [D-PA-12]",
        "lastName": "Lee",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Hazard Pay for Health Care Heroes Act",
    "type": "HR",
    "updateDate": "2026-05-13T19:24:49Z",
    "updateDateIncludingText": "2026-05-13T19:24:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:01:35Z",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "DC"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NJ"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "FL"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "VA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "HI"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "IN"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "WA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "IL"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NC"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "AL"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NY"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "WA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8484ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8484\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Ms. Lee of Pennsylvania (for herself, Mr. Khanna , Ms. Norton , Mrs. Watson Coleman , Mr. Frost , Mr. Garcia of California , Ms. McClellan , Ms. Tokuda , Ms. Crockett , Ms. Tlaib , Mr. Carson , Ms. Simon , Ms. Strickland , Mr. Jackson of Illinois , Mr. Casar , Ms. Pressley , Mrs. Foushee , Ms. Sewell , and Ms. Clarke of New York ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to provide for emergency grants to safeguard essential health care workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hazard Pay for Health Care Heroes Act .\n#### 2. Safeguarding essential health care workers\nThe Public Health Service Act is amended by inserting after section 319D\u20131 ( 42 U.S.C. 247d\u20134b ) the following:\n319D\u20132. Emergency grants to safeguard essential health care workers (a) Definitions In this section: (1) Emergency or disaster The term emergency or disaster means\u2014 (A) a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act; (B) an emergency declared by the President under section 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act; (C) a national emergency declared by the President under the National Emergencies Act; (D) a public health emergency declared under section 319; and (E) a State, local, territorial, or Tribal emergency or disaster, as declared by the applicable State, local, territorial, or Tribal government. (2) Eligible health care worker The term eligible health care worker means an essential health care worker whose work cannot be conducted remotely. (3) Essential health care worker The term essential health care worker means\u2014 (A) a health care provider, including a direct care worker (as defined in section 799B); (B) a medical technologist; (C) a public health worker; (D) an orderly (as defined in the 2010 Standard Occupational Classifications of the Department of Labor under the code for Orderlies (31\u20131015)); (E) an environmental service, janitorial, or custodial worker in a health care setting; and (F) any other professional role that the Secretary determines is essential to the care of patients or the maintenance of public health. (b) Grants (1) In general The Secretary may make grants to public or private nonprofit health care facilities and home health agencies for use in accordance with paragraph (2). (2) Use of funds (A) Hazardous duty compensation (i) In general The recipient of a grant under paragraph (1) shall use the grant funds to provide hazardous duty compensation to eligible health care workers for work performed during the period of an emergency or disaster in cases in which the Secretary determines that\u2014 (I) the performance of the work by the eligible health care worker for the applicable health care facility or home health agency is hazardous; or (II) the commute of the eligible health care worker is hazardous. (ii) Requirement (I) In general Subject to subclause (II), the amount of hazardous duty compensation under clause (i) shall be not more than $13 per hour, which shall be in addition to the wages or remuneration the eligible health care worker otherwise receives for the work. (II) Maximum amount The total amount of hazardous duty compensation received by any 1 eligible health care worker under this subparagraph may not exceed $25,000 per year. (B) Additional uses The recipient of a grant under paragraph (1) may use the grant funds to provide safety measures to safeguard and protect eligible health care workers from hazards due to the applicable emergency or disaster, including alternative transit options, personal protective equipment, and other safety measures. (c) Authorization of appropriations There are authorized to be appropriated to carry out this section such sums as may be necessary. .",
      "versionDate": "2026-04-23",
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
        "actionDate": "2026-04-21",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4357",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Hazard Pay for Health Care Heroes Act",
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
        "updateDate": "2026-05-13T19:24:48Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8484ih.xml"
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
      "title": "Hazard Pay for Health Care Heroes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T13:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hazard Pay for Health Care Heroes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T13:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to provide for emergency grants to safeguard essential health care workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T13:03:29Z"
    }
  ]
}
```
