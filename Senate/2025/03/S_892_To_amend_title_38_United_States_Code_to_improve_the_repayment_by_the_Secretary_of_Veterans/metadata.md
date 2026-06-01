# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/892?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/892
- Title: Veteran Fraud Reimbursement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 892
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2026-03-31T20:17:47Z
- Update date including text: 2026-03-31T20:17:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/892",
    "number": "892",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Veteran Fraud Reimbursement Act of 2025",
    "type": "S",
    "updateDate": "2026-03-31T20:17:47Z",
    "updateDateIncludingText": "2026-03-31T20:17:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
        "item": [
          {
            "date": "2025-03-11T14:30:24Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-06T19:29:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "AR"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "AZ"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s892is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 892\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Ms. Hirono (for herself, Mr. Boozman , Mr. Gallego , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the repayment by the Secretary of Veterans Affairs of benefits misused by a fiduciary, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veteran Fraud Reimbursement Act of 2025 .\n#### 2. Improvement to repayment by Secretary of Veterans Affairs of certain misused benefits\nSection 6107 of title 38, United States Code, is amended to read as follows:\n6107. Reissuance of benefits (a) Reissuance of misused benefits (1) In any case in which a fiduciary misuses all or part of an individual\u2019s benefit paid to such fiduciary, the Secretary shall pay to the beneficiary or the beneficiary\u2019s successor fiduciary an amount equal to the amount of such benefit so misused. (2) In any case in which the Secretary reissues a benefit payment (in whole or in part) under paragraph (1), the Secretary shall make a good faith effort to obtain recoupment from the fiduciary to whom the payment was originally made. (3) In any case in which the Secretary obtains recoupment from a fiduciary who has misused benefits, the Secretary shall promptly remit payment of the recouped amounts to the beneficiary or the beneficiary\u2019s successor fiduciary, as the case may be, to the extent that such amounts have not been paid under paragraph (1). (b) Reissuance of amounts in the case of a deceased beneficiary (1) If a beneficiary described in subsection (a)(1) predeceases a payment under such subsection, the Secretary shall pay such amount, subject to paragraph (2), to an individual or entity in accordance with section 5121 of this title. (2) The Secretary may not make a payment under this subsection to a fiduciary who misused benefits of the beneficiary. (c) Limitation on total amount paid The total of the amounts paid to a beneficiary or the beneficiary's successor fiduciary under this section may not exceed the total benefit amount misused by the fiduciary with respect to that beneficiary. (d) Oversight of negligence (1) The Secretary shall establish methods and timing with respect to determining whether an instance of misuse by a fiduciary, of all or part of an individual\u2019s benefit paid to such fiduciary, is the result of negligence by the Secretary. (2) The Secretary may not withhold the reissuing of a benefit payment under subsection (a)(1) by reason of a pending determination under paragraph (1). (3) The Secretary is not required to make a determination under paragraph (1) for each instance of misuse by a fiduciary, of all or part of an individual\u2019s benefit paid to such fiduciary. .",
      "versionDate": "2025-03-06",
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
        "actionDate": "2025-12-12",
        "text": "Became Public Law No: 119-56."
      },
      "number": "1912",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veteran Fraud Reimbursement Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-04-08T13:56:08Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-04-08T13:56:08Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-04-08T13:56:08Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-04-08T13:56:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T15:09:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
    "originChamber": "Senate",
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
          "measure-id": "id119s892",
          "measure-number": "892",
          "measure-type": "s",
          "orig-publish-date": "2025-03-06",
          "originChamber": "SENATE",
          "update-date": "2025-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s892v00",
            "update-date": "2025-05-21"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veteran Fraud Reimbursement Act of 2025</strong></p><p>This bill modifies the procedures by which the Department of Veterans Affairs (VA) reissues misused benefits to a beneficiary, including by requiring the VA to establish methods and timing with respect to determining whether an instance of misuse by a fiduciary is the result of negligence by the VA. The bill also provides that if a beneficiary predeceases a\u00a0reissuance, the VA must pay the amount to a surviving beneficiary in the same method as certain other VA benefits are paid upon the death of a beneficiary.</p><p>Under the bill, the VA may not withhold the reissuing of a benefit payment by reason of a pending determination regarding the VA's negligence in relation to the instance of misuse by a fiduciary. Additionally, the VA is not required to make a determination regarding its negligence for each instance of misuse by a fiduciary of all or part of an individual's benefit paid to such fiduciary.</p>"
        },
        "title": "Veteran Fraud Reimbursement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s892.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veteran Fraud Reimbursement Act of 2025</strong></p><p>This bill modifies the procedures by which the Department of Veterans Affairs (VA) reissues misused benefits to a beneficiary, including by requiring the VA to establish methods and timing with respect to determining whether an instance of misuse by a fiduciary is the result of negligence by the VA. The bill also provides that if a beneficiary predeceases a\u00a0reissuance, the VA must pay the amount to a surviving beneficiary in the same method as certain other VA benefits are paid upon the death of a beneficiary.</p><p>Under the bill, the VA may not withhold the reissuing of a benefit payment by reason of a pending determination regarding the VA's negligence in relation to the instance of misuse by a fiduciary. Additionally, the VA is not required to make a determination regarding its negligence for each instance of misuse by a fiduciary of all or part of an individual's benefit paid to such fiduciary.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119s892"
    },
    "title": "Veteran Fraud Reimbursement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veteran Fraud Reimbursement Act of 2025</strong></p><p>This bill modifies the procedures by which the Department of Veterans Affairs (VA) reissues misused benefits to a beneficiary, including by requiring the VA to establish methods and timing with respect to determining whether an instance of misuse by a fiduciary is the result of negligence by the VA. The bill also provides that if a beneficiary predeceases a\u00a0reissuance, the VA must pay the amount to a surviving beneficiary in the same method as certain other VA benefits are paid upon the death of a beneficiary.</p><p>Under the bill, the VA may not withhold the reissuing of a benefit payment by reason of a pending determination regarding the VA's negligence in relation to the instance of misuse by a fiduciary. Additionally, the VA is not required to make a determination regarding its negligence for each instance of misuse by a fiduciary of all or part of an individual's benefit paid to such fiduciary.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119s892"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s892is.xml"
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
      "title": "Veteran Fraud Reimbursement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veteran Fraud Reimbursement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to improve the repayment by the Secretary of Veterans Affairs of benefits misused by a fiduciary, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:54Z"
    }
  ]
}
```
