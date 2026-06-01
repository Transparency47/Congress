# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2541?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2541
- Title: Nuclear Medicine Clarification Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2541
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-01-06T23:32:07Z
- Update date including text: 2026-01-06T23:32:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2541",
    "number": "2541",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Nuclear Medicine Clarification Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-06T23:32:07Z",
    "updateDateIncludingText": "2026-01-06T23:32:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:03:00Z",
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
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "VA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "NC"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "NC"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "GA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "FL"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2541ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2541\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Davis of North Carolina (for himself, Mr. Griffith , and Mr. Cline ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Nuclear Regulatory Commission to revise its regulations to protect patients from unintended exposure to radiation during nuclear medicine procedures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nuclear Medicine Clarification Act of 2025 .\n#### 2. Medical event reporting of unintended irradiation\n##### (a) Revision of regulations required\nNot later than 120 days after the date of enactment of this Act, the Nuclear Regulatory Commission shall revise section 35.3045(a)(1) of title 10, Code of Federal Regulations, by adding at the end the following:\n(iv) A dose that is due to an extravasation and exceeds\u2014 (A) 0.5 Sv (50 rem) dose equivalent to the 5 cubic centimeter volume of tissue receiving the highest absorbed dose during residence time; or (B) 0.5 Sv (50 rem) shallow dose equivalent to the contiguous 10 square centimeters of skin receiving the highest absorbed dose during residence time. .\n##### (b) Effective date\nThe revision required under subsection (a) shall take effect on the date that is 18 months after the date of enactment of this Act.",
      "versionDate": "2025-04-01",
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
        "name": "Health",
        "updateDate": "2025-04-08T13:06:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119hr2541",
          "measure-number": "2541",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2026-01-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2541v00",
            "update-date": "2026-01-06"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Nuclear Medicine Clarification Act of 2025</strong></p><p>This bill requires the Nuclear Regulatory Commission (NRC) to revise its regulations so that health care providers must report to the NRC when a dose of a radioactive drug caused by an extravasation exceeds specified quantities. An <em>extravasation\u00a0</em>generally means the unintentional presence of a radioactive drug in the tissue surrounding the blood vessel following an injection.</p><p>Under the\u00a0NRC\u2019s current regulations, health care providers licensed by the NRC to use radioactive materials must submit a report to the NRC for any instance, known as a medical event, where the administered dose of a radioactive drug exceeds specified quantities or criteria.\u00a0</p><p>In 2024, the\u00a0NRC published a draft proposed rule that would add an extravasation as a medical event that must be reported. The draft proposed rule\u2019s reporting threshold is based on a physician\u2019s determination that the administration results or may potentially result in a radiation injury from an extravasation. The reporting threshold proposed by the\u00a0NRC does not contain a quantified dose.</p><p>The bill requires the\u00a0NRC to revise its regulations to add an extravasation as a medical event that must be reported, and it additionally requires the reporting threshold to be based on quantified doses (as specified in the bill). </p>"
        },
        "title": "Nuclear Medicine Clarification Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2541.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Nuclear Medicine Clarification Act of 2025</strong></p><p>This bill requires the Nuclear Regulatory Commission (NRC) to revise its regulations so that health care providers must report to the NRC when a dose of a radioactive drug caused by an extravasation exceeds specified quantities. An <em>extravasation\u00a0</em>generally means the unintentional presence of a radioactive drug in the tissue surrounding the blood vessel following an injection.</p><p>Under the\u00a0NRC\u2019s current regulations, health care providers licensed by the NRC to use radioactive materials must submit a report to the NRC for any instance, known as a medical event, where the administered dose of a radioactive drug exceeds specified quantities or criteria.\u00a0</p><p>In 2024, the\u00a0NRC published a draft proposed rule that would add an extravasation as a medical event that must be reported. The draft proposed rule\u2019s reporting threshold is based on a physician\u2019s determination that the administration results or may potentially result in a radiation injury from an extravasation. The reporting threshold proposed by the\u00a0NRC does not contain a quantified dose.</p><p>The bill requires the\u00a0NRC to revise its regulations to add an extravasation as a medical event that must be reported, and it additionally requires the reporting threshold to be based on quantified doses (as specified in the bill). </p>",
      "updateDate": "2026-01-06",
      "versionCode": "id119hr2541"
    },
    "title": "Nuclear Medicine Clarification Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Nuclear Medicine Clarification Act of 2025</strong></p><p>This bill requires the Nuclear Regulatory Commission (NRC) to revise its regulations so that health care providers must report to the NRC when a dose of a radioactive drug caused by an extravasation exceeds specified quantities. An <em>extravasation\u00a0</em>generally means the unintentional presence of a radioactive drug in the tissue surrounding the blood vessel following an injection.</p><p>Under the\u00a0NRC\u2019s current regulations, health care providers licensed by the NRC to use radioactive materials must submit a report to the NRC for any instance, known as a medical event, where the administered dose of a radioactive drug exceeds specified quantities or criteria.\u00a0</p><p>In 2024, the\u00a0NRC published a draft proposed rule that would add an extravasation as a medical event that must be reported. The draft proposed rule\u2019s reporting threshold is based on a physician\u2019s determination that the administration results or may potentially result in a radiation injury from an extravasation. The reporting threshold proposed by the\u00a0NRC does not contain a quantified dose.</p><p>The bill requires the\u00a0NRC to revise its regulations to add an extravasation as a medical event that must be reported, and it additionally requires the reporting threshold to be based on quantified doses (as specified in the bill). </p>",
      "updateDate": "2026-01-06",
      "versionCode": "id119hr2541"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2541ih.xml"
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
      "title": "Nuclear Medicine Clarification Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nuclear Medicine Clarification Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Nuclear Regulatory Commission to revise its regulations to protect patients from unintended exposure to radiation during nuclear medicine procedures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T04:18:28Z"
    }
  ]
}
```
