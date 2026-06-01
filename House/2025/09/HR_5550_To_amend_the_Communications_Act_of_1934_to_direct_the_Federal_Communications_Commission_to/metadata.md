# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5550?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5550
- Title: Lower Internet Costs Act
- Congress: 119
- Bill type: HR
- Bill number: 5550
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2025-12-16T19:23:42Z
- Update date including text: 2025-12-16T19:23:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-23: Introduced in House

## Actions

- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5550",
    "number": "5550",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Lower Internet Costs Act",
    "type": "HR",
    "updateDate": "2025-12-16T19:23:42Z",
    "updateDateIncludingText": "2025-12-16T19:23:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
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
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:00:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5550ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5550\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Mr. Harder of California introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Communications Act of 1934 to direct the Federal Communications Commission to promulgate regulations requiring providers of broadband service to state the aggregate price for such service and prohibiting providers of broadband service from charging certain fees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lower Internet Costs Act .\n#### 2. Statement of aggregate price for broadband service; certain fees prohibited\nTitle VII of the Communications Act of 1934 ( 47 U.S.C. 601 et seq. ) is amended by adding at the end the following:\n723. Statement of aggregate price for broadband service; certain fees prohibited (a) In general Not later than 90 days after the date of the enactment of this section, the Commission shall promulgate regulations that\u2014 (1) require a provider of broadband service\u2014 (A) to state the aggregate price for such service as a clear, easy-to-understand, and accurate single line item on the bill of a subscriber; and (B) if such provider communicates a price for such service in any promotional materials, to state the aggregate price for such service in a clear, easy-to-understand, and accurate manner in such materials; and (2) prohibit a provider of broadband service from charging a subscriber a covered fee. (b) Requirements regarding statement of aggregate price (1) On bill of subscriber With respect to the statement on the bill of a subscriber described in subsection (a)(1)(A) (including a bill for a legacy or grandfathered broadband service plan that is no longer generally available to new customers), the regulations promulgated under subsection (a) shall\u2014 (A) if the aggregate price stated is introductory or otherwise limited to a period of time, require the provider of broadband service to state on the bills provided to such subscriber approximately 60 days and 30 days before the end of such period\u2014 (i) either\u2014 (I) the length of such period; or (II) the date on which such period will end and the price charged will change; and (ii) the price that will be charged after the end of such period; and (B) permit the provider of broadband service to complement the aggregate price stated with an itemized explanation of the elements that compose such aggregate price. (2) In promotional materials With respect to the statement in any promotional materials described in subsection (a)(1)(B), the regulations promulgated under subsection (a) shall\u2014 (A) if the aggregate price stated is introductory or otherwise limited to a period of time, require the provider of broadband service to state in such materials\u2014 (i) the price that will be charged after the end of such period (calculated on the date on which such materials are made available to consumers); and (ii) the length of such period and the length of time for which the price described in clause (i) will be charged; (B) if part of the aggregate price stated fluctuates based on service location, require the provider of broadband service to state where and how a consumer may obtain the aggregate price specific to such consumer (such as electronically or by contacting a customer service or sales representative); (C) permit the provider of broadband service to complement the aggregate price stated with an itemized explanation of the elements that compose such aggregate price; and (D) specify that the requirements in such regulations with respect to such statement do not apply with respect to legacy or grandfathered broadband service plans that are no longer generally available to new customers. (3) Exclusions from aggregate price The regulations promulgated under subsection (a) shall specify other charges related to the provision of broadband service (such as taxes, administrative fees, and equipment fees) that are not charged for the broadband service itself and are not required to be included in the aggregate price stated under such regulations. (4) Application to bundled services The regulations promulgated under subsection (a) shall provide that, if a provider of broadband service bills for or promotes broadband service as part of a bundle with other services\u2014 (A) the statements described in subsection (a)(1) are required with respect to any charges for such bundle that are specific to broadband service; and (B) the prohibition on charging a covered fee under subsection (a)(2) applies with respect to all services that are part of such bundle. (c) Definitions In this section: (1) Broadband service The term broadband service has the meaning given the term broadband internet access service in section 8.1(b) of title 47, Code of Federal Regulations (or any successor regulation). (2) Covered fee The term covered fee means, with respect to a fee charged by a provider of broadband service, the following: (A) A fee to cover the cost of compliance with State regulations and programs (commonly known as a State cost recovery charge ). (B) A fee to cover the cost of maintaining, building, or operating the network of such provider (commonly known as a network access and maintenance fee , internet cost recovery fee , broadband cost recovery fee , or network enhancement fee ). (C) A fee imposed by a local government on such provider to compensate such local government for use of a public right-of-way (commonly known as a local access fee ). (D) A fee for the cost of technical support or repair of equipment (commonly known as a tech assure fee ). (E) Any other fee determined by the Commission to be charged for a purpose similar to a purpose described in any of subparagraphs (A) through (D). .",
      "versionDate": "2025-09-23",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-16T19:23:41Z"
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
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5550ih.xml"
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
      "title": "Lower Internet Costs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lower Internet Costs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T06:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Communications Act of 1934 to direct the Federal Communications Commission to promulgate regulations requiring providers of broadband service to state the aggregate price for such service and prohibiting providers of broadband service from charging certain fees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T06:18:26Z"
    }
  ]
}
```
