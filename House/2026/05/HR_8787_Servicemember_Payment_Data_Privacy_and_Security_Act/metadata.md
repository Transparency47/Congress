# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8787?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8787
- Title: Servicemember Payment Data Privacy and Security Act
- Congress: 119
- Bill type: HR
- Bill number: 8787
- Origin chamber: House
- Introduced date: 2026-05-13
- Update date: 2026-05-27T08:53:39Z
- Update date including text: 2026-05-27T08:53:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-13: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-05-13: Introduced in House

## Actions

- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8787",
    "number": "8787",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Servicemember Payment Data Privacy and Security Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:53:39Z",
    "updateDateIncludingText": "2026-05-27T08:53:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "MI"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "AL"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "AZ"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "TX"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "WI"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "AZ"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-05-22",
      "state": "GA"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8787ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8787\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2026 Mr. Cline (for himself, Mr. Moolenaar , Mr. Moore of Alabama , Mr. Crane , Mr. Self , and Mr. Fitzgerald ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo prohibit the Secretary of Defense from contracting with retailers who use covered payment processing equipment, systems, or services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Servicemember Payment Data Privacy and Security Act .\n#### 2. Elimination of use of certain payment processing equipment, systems, or services\n##### (a) Review\nNot later than 180 days after the date of the enactment of this section, the Secretary of Defense shall complete a review of all retailers to determine if such retailers use covered equipment, systems, or services as a substantial or essential component of the performance of a contract to provide payment processing equipment, systems, or services for the Department of Defense.\n##### (b) Guidance\nNot later than 90 days after completing the review required by subsection (a), the Secretary of Defense shall issue guidance prohibiting the use of covered equipment, systems, or services by a retailer in a contract with the Department of Defense. Such policy and guidance shall direct the modification or termination of such a contract unless the retailer for such contract ceases use of covered equipment, systems, or services in a timely manner.\n##### (c) Prohibition\nEffective January 1, 2027, the Secretary of Defense may not enter into a contract for payment processing equipment, systems, or services with a retailer that uses covered equipment, systems, or services as a substantial or essential component of the performance of such contract.\n##### (d) Report\nNot later than one year after the date of the enactment of this section, the Secretary of Defense shall submit to the Committees on Armed Services of the House of Representatives and the Senate a written report on the implementation on the requirements of this section.\n##### (e) Definitions\nIn this section:\n**(1) Country of concern**\nThe term country of concern means\u2014\n**(A)**\nChina;\n**(B)**\nRussia;\n**(C)**\nthe Islamic Republic of Iran;\n**(D)**\nNorth Korea; and\n**(E)**\nany other country designated by the Secretary of Defense, as posing a significant risk to the national security of the United States.\n**(2) Covered equipment, system, or service**\nThe term covered equipment, system, or service \u2014\n**(A)**\nmeans a payment processing equipment, system, or service for which the application processor, source code, secure processor, or secure firmware is directly or indirectly developed, manufactured, provided, owned, controlled, or operated by\u2014\n**(i)**\nan entity organized under the laws of a country of concern;\n**(ii)**\nan entity owned or controlled by the government of a country of concern;\n**(iii)**\nan entity subject to the direction, jurisdiction, or control of the government, military, or intelligence services of a country of concern;\n**(iv)**\nany subsidiary, affiliate, or successor entity of an entity described in clauses (i) through (iii); or\n**(v)**\nan entity that the Secretary of Defense reasonably believes to be an entity owned or controlled by, or otherwise connected entity owned or controlled by a country of concern; and\n**(B)**\nincludes payment processing equipment, systems, or services substantially comprised of components, software, or technology supplied by an entity described in any of clauses (i) through (v) of subparagraph (A).\n**(3) Electronic fund transfer**\nThe term electronic fund transfer \u2014\n**(A)**\nmeans any transfer of funds, other than a transaction originated by check, draft, or similar paper instrument, which is initiated through an electronic terminal (as defined in section 903 of the Electronic Fund Transfer Act ( 15 U.S.C. 1693a )), telephone, or computer or magnetic tape so as to order, instruct, or authorize a financial institution to debit or credit an account; and\n**(B)**\nincludes point-of-sale transfers, automated teller machine transactions, and direct deposits or withdrawals of funds from an account.\n**(4) Payment processing equipment, system, or service**\nThe term payment processing equipment, system, or service means\u2014\n**(A)**\na card, code, or other means of access to a consumer\u2019s account, or any combination thereof, that may be used by the consumer to initiate electronic fund transfers; or\n**(B)**\nan electronic device, other than a telephone operated by a consumer, through which a consumer may initiate an electronic fund transfer.\n**(5) Retailer**\nThe term retailer has the meaning given in section 4664 of title 10, United States Code.",
      "versionDate": "2026-05-13",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8787ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Servicemember Payment Data Privacy and Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-27T08:53:39Z"
    },
    {
      "title": "Servicemember Payment Data Privacy and Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:53:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Secretary of Defense from contracting with retailers who use covered payment processing equipment, systems, or services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:48:35Z"
    }
  ]
}
```
