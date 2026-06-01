# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5981?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5981
- Title: VA Billing Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 5981
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-12-11T09:07:39Z
- Update date including text: 2025-12-11T09:07:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5981",
    "number": "5981",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "VA Billing Accountability Act",
    "type": "HR",
    "updateDate": "2025-12-11T09:07:39Z",
    "updateDateIncludingText": "2025-12-11T09:07:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:35:55Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NC"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "AZ"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "WA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-11-13",
      "state": "MN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5981ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5981\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mr. Smucker (for himself, Mr. Davis of North Carolina , Mr. Ciscomani , and Mr. Newhouse ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to waive the requirement of certain veterans to make copayments for hospital care and medical services in the case of an error by the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Billing Accountability Act .\n#### 2. Authority of Secretary of Veterans Affairs to waive requirement of certain veterans to make copayments for care and services in the case of Department of Veterans Affairs error\n##### (a) Hospital care, nursing home care, and medical services\nSection 1710(f)(3) of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(G) During the two-year period following the date of the enactment of the VA Billing Accountability Act , the Secretary may waive the requirement of a veteran to make a payment under this subsection or subsection (g) if\u2014 (i) an error committed by the Department or an employee of the Department was the cause of delaying notification sent to the veteran of the requirement to make the payment; and (ii) the veteran received such notification later than 180 days after the date on which the veteran received the care or services for which the payment was required. .\n##### (b) Medications\nSection 1722A of such title is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following new subsection (c):\n(c) During the two-year period following the date of the enactment of the VA Billing Accountability Act , the Secretary may waive the requirement of a veteran to make a payment under this section if\u2014 (1) an error committed by the Department or an employee of the Department was the cause of delaying notification sent to the veteran of the requirement to make the payment; and (2) the veteran received such notification later than 180 days after the date on which the veteran received the medication for which the payment was required. .\n##### (c) Billing procedures\n**(1) In general**\nSubchapter I of chapter 17 of such title is amended by adding at the end the following new section:\n1709D. Procedures for copayments (a) Care at Department facility (1) In requiring a veteran to make a payment for care or services provided at a medical facility of the Department pursuant to this chapter, including sections 1710 and 1722A, the Secretary shall provide to such veteran a notification of such required payment by not later than 180 days after the date on which the veteran receives the care or services for which payment is required. (2) If the Secretary does not provide to a veteran a notification of the required payment by the date required under paragraph (1), the Secretary may not collect such payment, including through a third-party entity, unless the Secretary provides the veteran the following: (A) Information regarding how to apply for a waiver described in section 1710(f)(3)(G) or section 1722A(c) of this title, as appropriate. (B) Information regarding how to establish a payment plan with the Secretary. (C) Opportunity to make such a waiver or establish such a payment plan. (b) Care at non-Department facility (1) In requiring a veteran to make a payment for care or services provided at a non-Department facility pursuant to this chapter or other provision of law, the Secretary shall provide to such veteran a notification of such required payment by not later than 18 months after the date on which the veteran receives the care or services for which payment is required. (2) If the Secretary does not provide to a veteran a notification of the required payment by the date required under paragraph (1), the Secretary may not collect such payment, including through a third-party entity, unless the Secretary provides the veteran the following: (A) Information regarding how to apply for a waiver described in paragraph (3). (B) Information regarding how to establish a payment plan with the Secretary. (C) Opportunity to make such a waiver or establish such a payment plan. (3) The Secretary may waive the requirement of a veteran to make a payment for care or services provided at a non-Department facility pursuant to this chapter or other provision of law if\u2014 (A) an error committed by the Department, an employee of the Department, or a non-Department facility was the cause of delaying the notification sent to the veteran of the requirement to make the payment; and (B) the veteran received such notification after the period described in paragraph (1). (c) Waivers The Secretary shall review cases under which the Secretary issues waivers under this section to determine how to reduce the number of notifications issued after the periods established in this section. (d) Termination This section shall cease to be effective on the day that is two years after the date of the enactment of the VA Billing Accountability Act . .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1709C the following new item:\n1709D. Procedures for copayments. .\n##### (d) Improvement of procedures\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall\u2014\n**(1)**\nreview the copayment billing internal controls and notification procedures of the Department of Veterans Affairs; and\n**(2)**\nimprove such controls and procedures, including pursuant to the amendments made by this Act.",
      "versionDate": "2025-11-07",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-18T15:58:54Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5981ih.xml"
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
      "title": "VA Billing Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Billing Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to waive the requirement of certain veterans to make copayments for hospital care and medical services in the case of an error by the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T09:48:15Z"
    }
  ]
}
```
