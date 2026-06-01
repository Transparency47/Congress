# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1418?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1418
- Title: Purchased and Referred Care Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1418
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2025-05-14T14:16:33Z
- Update date including text: 2025-05-14T14:16:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1418",
    "number": "1418",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Purchased and Referred Care Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-14T14:16:33Z",
    "updateDateIncludingText": "2025-05-14T14:16:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-18T18:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "WA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "CO"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "WA"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OK"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "WA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1418ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1418\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Johnson of South Dakota (for himself and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Indian Health Care Improvement Act to address liability for payment of charges or costs associated with provision of purchased/referred care services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Purchased and Referred Care Improvement Act of 2025 .\n#### 2. Changes to liability for payment\n##### (a) In general\nSection 222 of the Indian Health Care Improvement Act ( 25 U.S.C. 1621u ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking A patient and inserting Notwithstanding any other provision of law or any agreement, form, or other written or electronic document signed by a patient, a patient ; and\n**(B)**\nby striking contract health care and inserting purchased/referred care ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking contract care each place it appears and inserting purchased/referred care ;\n**(B)**\nby striking contract health care and inserting purchased/referred care ;\n**(C)**\nby inserting , notwithstanding any other provision of law or any agreement, form, or other written or electronic document signed by a patient, after by the Service that ; and\n**(D)**\nby inserting to any provider, debt collector, or any other person after is not liable ;\n**(3)**\nin subsection (c), by inserting , the debt collector, or any other person, as applicable after the provider ; and\n**(4)**\nby adding at the end the following:\n(d) Reimbursement (1) In general Not later than 120 days after the date of the enactment of this subsection and in consultation with Indian Tribes, the Secretary shall establish and implement procedures to allow a patient that paid out-of-pocket for purchased/referred care services authorized by the Service under this Act to be reimbursed by the Service for that payment not later than 30 days after the patient submits documentation to the Service pursuant to paragraph (2). (2) Submitting documentation The Secretary shall accept documentation from a patient seeking reimbursement under paragraph (1) that was submitted\u2014 (A) electronically; or (B) in-person at a Service facility. (3) Effect The preceding provisions of this subsection shall not apply to purchased/referred care service furnished under a purchased/referred care services program operated by an Indian Tribe under an Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5301 et seq. ) compact or contract unless expressly agreed to by the Indian Tribe. (e) Updating authorities Not later than 180 days of the enactment of this subsection and in consultation with Indian Tribes, the Secretary shall update applicable provisions of and exhibits to the Indian Health Manual, contracts with providers, and other relevant documents and administrative authorities to incorporate the provisions of this section. .\n##### (b) Application\nThe amendments made by this section shall apply to purchased/referred care services authorized by the Indian Health Service furnished on, before, or after the date of the enactment of this Act.\n#### 3. Technical amendments\n##### (a) Definitions\nSection 4(5) of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 ) is amended by striking the paragraph designation and heading and all that follows through means and inserting the following:\n(5) Purchased/referred care The term purchased/referred care means .\n##### (b) Technical amendments\nThe Indian Health Care Improvement Act ( 25 U.S.C. 1601 et seq. ) is amended by striking contract health service each place it appears (regardless of casing and typeface and including in the headings) and inserting purchased/referred care (with appropriate casing and typeface).\n##### (c) Updating authorities\nThe Secretary of Health and Human Services is directed to ensure that the Indian Health Manual and all other relevant rules, guidance, manuals, and other materials are revised such that contract health service , each place it appears (regardless of casing and typeface and including in the headings) is revised to read purchased/referred care (with appropriate casing and typeface).",
      "versionDate": "2025-02-18",
      "versionType": "Introduced in House"
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
        "name": "Native Americans",
        "updateDate": "2025-05-08T19:00:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1418",
          "measure-number": "1418",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1418v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Purchased and Referred Care Improvement Act of 2025</strong></p><p>This bill specifies that the Indian Health Service (IHS) must reimburse patients for their out-of-pocket costs for authorized purchased/referred care services within 30 days. (The IHS provides medical and dental services directly to American Indian and Alaska Native patients whenever possible. However, when services are not available, IHS beneficiaries may be referred to private providers. This is called purchased/referred care.)</p><p>Specifically, the bill requires the Department of Health and Human Services (HHS) to establish and implement procedures to allow a patient who paid out of pocket for purchased/referred care services authorized by the IHS to be reimbursed by the IHS for that payment no later than 30 days after the patient submits required documentation.\u00a0</p><p>Additionally, the bill requires HHS to\u00a0update applicable provisions of and exhibits to the Indian Health Manual, contracts with providers, and other relevant documents and administrative authorities to incorporate the provisions of the bill.</p><p>The bill also replaces statutory references to <em>contract health service</em> with <em>purchased/referred care</em>.</p>"
        },
        "title": "Purchased and Referred Care Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1418.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Purchased and Referred Care Improvement Act of 2025</strong></p><p>This bill specifies that the Indian Health Service (IHS) must reimburse patients for their out-of-pocket costs for authorized purchased/referred care services within 30 days. (The IHS provides medical and dental services directly to American Indian and Alaska Native patients whenever possible. However, when services are not available, IHS beneficiaries may be referred to private providers. This is called purchased/referred care.)</p><p>Specifically, the bill requires the Department of Health and Human Services (HHS) to establish and implement procedures to allow a patient who paid out of pocket for purchased/referred care services authorized by the IHS to be reimbursed by the IHS for that payment no later than 30 days after the patient submits required documentation.\u00a0</p><p>Additionally, the bill requires HHS to\u00a0update applicable provisions of and exhibits to the Indian Health Manual, contracts with providers, and other relevant documents and administrative authorities to incorporate the provisions of the bill.</p><p>The bill also replaces statutory references to <em>contract health service</em> with <em>purchased/referred care</em>.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr1418"
    },
    "title": "Purchased and Referred Care Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Purchased and Referred Care Improvement Act of 2025</strong></p><p>This bill specifies that the Indian Health Service (IHS) must reimburse patients for their out-of-pocket costs for authorized purchased/referred care services within 30 days. (The IHS provides medical and dental services directly to American Indian and Alaska Native patients whenever possible. However, when services are not available, IHS beneficiaries may be referred to private providers. This is called purchased/referred care.)</p><p>Specifically, the bill requires the Department of Health and Human Services (HHS) to establish and implement procedures to allow a patient who paid out of pocket for purchased/referred care services authorized by the IHS to be reimbursed by the IHS for that payment no later than 30 days after the patient submits required documentation.\u00a0</p><p>Additionally, the bill requires HHS to\u00a0update applicable provisions of and exhibits to the Indian Health Manual, contracts with providers, and other relevant documents and administrative authorities to incorporate the provisions of the bill.</p><p>The bill also replaces statutory references to <em>contract health service</em> with <em>purchased/referred care</em>.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr1418"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1418ih.xml"
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
      "title": "Purchased and Referred Care Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Purchased and Referred Care Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Indian Health Care Improvement Act to address liability for payment of charges or costs associated with provision of purchased/referred care services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:24Z"
    }
  ]
}
```
