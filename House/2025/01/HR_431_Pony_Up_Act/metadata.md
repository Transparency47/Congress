# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/431?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/431
- Title: Pony Up Act
- Congress: 119
- Bill type: HR
- Bill number: 431
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-07-07T16:34:55Z
- Update date including text: 2025-07-07T16:34:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/431",
    "number": "431",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000546",
        "district": "6",
        "firstName": "Sam",
        "fullName": "Rep. Graves, Sam [R-MO-6]",
        "lastName": "Graves",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Pony Up Act",
    "type": "HR",
    "updateDate": "2025-07-07T16:34:55Z",
    "updateDateIncludingText": "2025-07-07T16:34:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "MO"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MO"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "IL"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "GA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MN"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "KS"
    },
    {
      "bioguideId": "S001195",
      "district": "8",
      "firstName": "Jason",
      "fullName": "Rep. Smith, Jason [R-MO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MO"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MO"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KY"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr431ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 431\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Graves (for himself, Mr. Cleaver , Mr. Alford , Mr. Bost , Mr. Collins , Mr. Stauber , and Mr. Mann ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the United States Postal Service to reimburse fees charged for the late payment of bills that were delayed in the mail, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pony Up Act .\n#### 2. Payment of fees resulting from delayed delivery\n##### (a) In general\nExcept as otherwise provided in this section, the United States Postal Service shall pay to a citizen assessed any fee or penalty for the late payment of a bill an amount determined under subsection (b) if such bill, notice of such bill, or payment is delivered late.\n##### (b) Payment calculation\nThe amount to which a citizen is entitled under subsection (a) is the amount that is equal to the total amount of the fees and penalties described in such subsection that such citizen is obligated to pay.\n##### (c) Application\n**(1) In general**\nA citizen seeking a payment under this section shall submit to the United States Postal Service an application at such time, in such manner, and containing such information as the United States Postal Service determines appropriate.\n**(2) Application submission**\nThe United States Postal Service shall allow citizens to submit the application required by paragraph (1) on a publicly available website of the United States Postal Service, by mail, and at any post office.\n##### (d) Unforeseen circumstances exception\nFor the purposes of this section, a bill, notice of bill, or payment is not delivered late if a cause not reasonably within the control of the United States Postal Service delayed the delivery of such bill or notice, including a major disaster or emergency declared by the President.\n##### (e) Appeals\n**(1) In general**\nA citizen may appeal a determination made by the United States Postal Service under this section to the Judicial Officer by submitting such appeal in writing within 30 days after receiving notice of such determination.\n**(2) Procedure**\nThe Judicial Officer shall issue a decision with respect to an appeal under paragraph (1) as soon as practicable, and such decision shall be final.\n##### (f) Regulations\nNot later than 60 days after the date of enactment of this Act, the United States Postal Service shall issue rules implementing this section.\n##### (g) Definitions\nIn this section:\n**(1) Delivered late**\nThe term delivered late , with respect to a bill, notice of bill, or payment, means that\u2014\n**(A)**\nsuch bill, notice, or payment was mailed;\n**(B)**\nin the case of a bill or notice of bill, the United States Postal Service received the mail containing such bill or notice not less than 12 days prior to the date on which the payment for the bill was due and the United States Postal Service delivered such mail less than 6 days prior to the date on which payment for the bill was due; and\n**(C)**\nin the case of a payment, the United States Postal Service received the mail containing such payment not less than 5 days prior to the date on which the payment was due and the United States Postal Service delivered such mail after the date on which payment was due.\n**(2) Judicial officer**\nThe term Judicial Officer means the Judicial Officer appointed under section 204 of title 39, United States Code.\n#### 3. Report on mail delivery delays\n##### (a) Annual report\nNot later than one year after the date of enactment of this Act, and annually thereafter, the United States Postal Service shall submit to the Committee on Oversight and Government Reform of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on delays in delivering mail, including, for each class of mail\u2014\n**(1)**\nthe average delivery time and average delay time for\u2014\n**(A)**\nmail delivered under an agreement between the sender, other than a sender primarily engaged in the transportation or delivery of parcels or letters carried out of the mails, and the United States Postal Service; and\n**(B)**\nall other mail delivered by the United States Postal Service;\n**(2)**\nthe volume of mail described in paragraph (1)(A) that is presorted and an explanation of the effect of presorting such mail on the average delivery time and average delay time for such mail; and\n**(3)**\nthe volume of mail described in paragraph (1)(B) that is presorted and an explanation of the effect of presorting such mail on the average delivery time and average delay time for such mail.\n##### (b) Prioritization audit\n**(1) In general**\nThe Inspector General of the United States Postal Service shall conduct an assessment of the policies and practices of the United States Postal Service to determine if the United States Postal Service prioritizes the delivery of mail described in subsection (a)(1)(A) over mail that is the same class of mail and is not described in such subsection.\n**(2) Report**\nNot later than one year after the date of enactment of this Act, the Inspector General of the United States Postal Service shall submit to the Committee on Oversight and Government Reform of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on the findings of the assessment required by paragraph (1).\n##### (c) Class of mail defined\nFor the purposes of this section, the term class of mail means the items described in paragraphs (1) through (10) of section 3621(a) of title 5, United States Code, and the items described in paragraphs (1) through (5) of section 3631(a) of such title.",
      "versionDate": "2025-01-15",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2025-02-26T14:43:28Z"
          },
          {
            "name": "Administrative remedies",
            "updateDate": "2025-02-26T14:43:15Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-26T14:43:24Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-26T14:43:20Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-02-26T14:43:01Z"
          },
          {
            "name": "U.S. Postal Service",
            "updateDate": "2025-02-26T14:43:09Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-02-26T14:43:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-19T16:01:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr431",
          "measure-number": "431",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-07-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr431v00",
            "update-date": "2025-07-07"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pony Up Act</strong></p><p>This bill requires the U.S. Postal Service (USPS) to pay a citizen for late payment fees or penalties incurred due to late delivery of mail by USPS.</p><p>Late delivery of mail means that (1) USPS received a bill or notice of bill at least 12 days prior to the payment due date and delivered such bill or notice of bill less than 6 days prior to the payment due date; or (2) USPS received a payment at least 5 days prior to the payment due date and delivered such payment after the due date.\u00a0</p><p>USPS is not required to pay a citizen for late payment fees or penalties when a bill, notice of bill, or payment is delayed for reasons outside of USPS control (for example, if a major disaster or emergency declared by the President caused the delay).</p>"
        },
        "title": "Pony Up Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr431.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pony Up Act</strong></p><p>This bill requires the U.S. Postal Service (USPS) to pay a citizen for late payment fees or penalties incurred due to late delivery of mail by USPS.</p><p>Late delivery of mail means that (1) USPS received a bill or notice of bill at least 12 days prior to the payment due date and delivered such bill or notice of bill less than 6 days prior to the payment due date; or (2) USPS received a payment at least 5 days prior to the payment due date and delivered such payment after the due date.\u00a0</p><p>USPS is not required to pay a citizen for late payment fees or penalties when a bill, notice of bill, or payment is delayed for reasons outside of USPS control (for example, if a major disaster or emergency declared by the President caused the delay).</p>",
      "updateDate": "2025-07-07",
      "versionCode": "id119hr431"
    },
    "title": "Pony Up Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pony Up Act</strong></p><p>This bill requires the U.S. Postal Service (USPS) to pay a citizen for late payment fees or penalties incurred due to late delivery of mail by USPS.</p><p>Late delivery of mail means that (1) USPS received a bill or notice of bill at least 12 days prior to the payment due date and delivered such bill or notice of bill less than 6 days prior to the payment due date; or (2) USPS received a payment at least 5 days prior to the payment due date and delivered such payment after the due date.\u00a0</p><p>USPS is not required to pay a citizen for late payment fees or penalties when a bill, notice of bill, or payment is delayed for reasons outside of USPS control (for example, if a major disaster or emergency declared by the President caused the delay).</p>",
      "updateDate": "2025-07-07",
      "versionCode": "id119hr431"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr431ih.xml"
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
      "title": "Pony Up Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pony Up Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T12:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the United States Postal Service to reimburse fees charged for the late payment of bills that were delayed in the mail, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T12:48:17Z"
    }
  ]
}
```
