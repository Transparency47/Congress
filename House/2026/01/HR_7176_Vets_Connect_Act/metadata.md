# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7176?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7176
- Title: Vets Connect Act
- Congress: 119
- Bill type: HR
- Bill number: 7176
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-02-11T13:31:50Z
- Update date including text: 2026-02-11T13:31:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7176",
    "number": "7176",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "E000246",
        "district": "11",
        "firstName": "Chuck",
        "fullName": "Rep. Edwards, Chuck [R-NC-11]",
        "lastName": "Edwards",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Vets Connect Act",
    "type": "HR",
    "updateDate": "2026-02-11T13:31:50Z",
    "updateDateIncludingText": "2026-02-11T13:31:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7176ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7176\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Mr. Edwards (for himself and Ms. Budzinski ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the Secretary of Veterans Affairs to establish a secure database and messaging platform to enable veterans to reconnect with other veterans with whom they served, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Vets Connect Act .\n#### 2. Vets Connect secure database and messaging platform\n##### (a) Establishment of secure database and messaging platform\nThe Secretary of Veterans Affairs shall establish and maintain a secure, privacy-preserving database and messaging platform (in this section referred to as the Vets Connect System ) for the purpose of enabling veterans to reconnect with other veterans with whom they served, without disclosing personal contact information such as phone numbers, email addresses, physical addresses, or social media identifiers unless expressly authorized by the veteran.\n##### (b) Content of system\nThe Secretary shall ensure that the Vets Connect System includes only the minimum information necessary to facilitate service-based matching between veterans, including\u2014\n**(1)**\nservice-connection information, such as branch of service, units, dates of service, deployments, occupational specialty, and rank;\n**(2)**\na display name selected by the veteran, which need not contain the veteran\u2019s legal name; and\n**(3)**\nany additional information the veteran elects to include for visibility within the System by taking an affirmative, documented opt-in action executed within the System.\n##### (c) Use within Department\nInformation contained in the Vets Connect System may not be used by the Department for any purpose other than operating, securing, and overseeing the System.\n##### (d) Access limited to verified veterans\nExcept for access required by subsection (c), the Secretary shall ensure that\u2014\n**(1)**\naccess to the Vets Connect System is limited to individuals whose military service has been verified by the Department of Veterans Affairs or the Department of Defense; and\n**(2)**\nno individual whose service has not been verified may gain access.\n##### (e) Information about veterans only if they opt in\nThe Secretary shall ensure that\u2014\n**(1)**\nno veteran appears in search results or is discoverable by other users unless the veteran has affirmatively opted in to participation in the System; and\n**(2)**\nno veteran\u2019s personal contact information is stored in, displayed through, or retrievable from the Vets Connect System, or disclosed through the messaging platform within the System, except to the extent the veteran takes an affirmative, documented opt-in action executed within the System.\n##### (f) Options to opt-Out\nThe Secretary shall ensure that a veteran may at any time\u2014\n**(1)**\nchange their visibility settings;\n**(2)**\nrestrict communications from some or all other users;\n**(3)**\nopt out of participation in the System; or\n**(4)**\ndelete any information the veteran has contributed to the System.\n##### (g) Prohibition on commercial solicitation and data brokerage\n**(1) In general**\nNo veteran or other person or entity may use information contained in or derived from the Vets Connect System for\u2014\n**(A)**\nsolicitation of legal, financial, or claims-related services;\n**(B)**\nadvertising, marketing, or commercial outreach; or\n**(C)**\nany data-brokerage activity, including the sale, transfer, licensing, or aggregation of user information.\n**(2) Contractors, subcontractors, and third parties**\nNo contractor, subcontractor, or third party may use System data for any purpose other than performing duties under a contract with the Department.\n##### (h) Security, audit logs, and oversight\n**(1) Security**\nThe Secretary shall implement industry-standard cybersecurity protections, including encryption, access controls, and monitoring, to prevent unauthorized access, scraping, mass-messaging, or harvesting of veteran data in the System.\n**(2) Audit logs**\nThe Secretary shall maintain system-level audit logs documenting all access, queries, administrative actions, and communications metadata (but not message content) for the purpose of oversight.\n**(3) Oversight**\nThe Inspector General of the Department of Veterans Affairs shall have access to such audit logs and may conduct periodic reviews of compliance, security controls, and misuse prevention.\n##### (i) Penalties for misuse\nAny individual who knowingly accesses, attempts to access, or uses information in the Vets Connect System for a prohibited purpose or otherwise violates this section shall be subject to such penalties as the Secretary may prescribe by regulation and any other penalties available under law, including section 5701 of title 38, United States Code, if applicable.\n##### (j) Rule of construction\nNothing in this section shall be construed to authorize the disclosure of any record protected under section 5701 of title 38, United States Code, or any other privacy or security law applicable to the Department of Veterans Affairs.",
      "versionDate": "2026-01-21",
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
        "updateDate": "2026-02-11T13:31:50Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7176ih.xml"
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
      "title": "Vets Connect Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Vets Connect Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require the Secretary of Veterans Affairs to establish a secure database and messaging platform to enable veterans to reconnect with other veterans with whom they served, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T04:48:19Z"
    }
  ]
}
```
