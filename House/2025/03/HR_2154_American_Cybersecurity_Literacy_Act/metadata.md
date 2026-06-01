# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2154?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2154
- Title: American Cybersecurity Literacy Act
- Congress: 119
- Bill type: HR
- Bill number: 2154
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-12-17T09:06:31Z
- Update date including text: 2025-12-17T09:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2154",
    "number": "2154",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "American Cybersecurity Literacy Act",
    "type": "HR",
    "updateDate": "2025-12-17T09:06:31Z",
    "updateDateIncludingText": "2025-12-17T09:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:00:05Z",
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
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "VA"
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
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2154ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2154\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Obernolte (for himself and Ms. McClellan ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish a cybersecurity literacy campaign, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Cybersecurity Literacy Act .\n#### 2. Sense of Congress\nIt is the sense of the Congress that the United States has a national security and economic interest in promoting cybersecurity literacy amongst the general public.\n#### 3. Establishment of cybersecurity literacy campaign\n##### (a) In general\nThe Assistant Secretary shall develop and conduct a cybersecurity literacy campaign (which shall be available in multiple languages and formats, if practicable) to increase the knowledge and awareness of the American people of best practices to reduce cybersecurity risks.\n##### (b) Campaign requirements\nIn carrying out subsection (a), the Assistant Secretary shall\u2014\n**(1)**\neducate the American people on how to prevent and mitigate cyberattacks and cybersecurity risks, including by\u2014\n**(A)**\ninstructing the American people on how to identify\u2014\n**(i)**\nphishing emails and messages; and\n**(ii)**\nsecure websites;\n**(B)**\ninstructing the American people about the benefits of changing default passwords on hardware and software technology;\n**(C)**\nencouraging the use of cybersecurity tools, including\u2014\n**(i)**\nmulti-factor authentication;\n**(ii)**\ncomplex passwords;\n**(iii)**\nanti-virus software;\n**(iv)**\npatching and updating software and applications; and\n**(v)**\nvirtual private networks;\n**(D)**\nidentifying the devices that could pose possible cybersecurity risks, including\u2014\n**(i)**\npersonal computers;\n**(ii)**\nsmartphones;\n**(iii)**\ntablets;\n**(iv)**\nWi-Fi routers;\n**(v)**\nsmart home appliances;\n**(vi)**\nwebcams;\n**(vii)**\ninternet-connected monitors; and\n**(viii)**\nany other device that can be connected to the internet, including mobile devices other than smartphones and tablets;\n**(E)**\nencouraging Americans to\u2014\n**(i)**\nregularly review mobile application permissions;\n**(ii)**\ndecline privilege requests from mobile applications that are unnecessary;\n**(iii)**\ndownload applications only from trusted vendors or sources; and\n**(iv)**\nconsider a product\u2019s life cycle and the developer or manufacturer\u2019s commitment to providing security updates during a connected device\u2019s expected period of use; and\n**(F)**\nidentifying the potential cybersecurity risks of using publicly available Wi-Fi networks and the methods a user may utilize to limit such risks; and\n**(2)**\nencourage the American people to use resources to help mitigate the cybersecurity risks identified in this subsection.\n##### (c) Assistant Secretary defined\nIn this section, the term Assistant Secretary means the Assistant Secretary of Commerce for Communications and Information.",
      "versionDate": "2025-03-14",
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
        "updateDate": "2025-04-01T17:41:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2154",
          "measure-number": "2154",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-09-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2154v00",
            "update-date": "2025-09-15"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>American Cybersecurity Literacy Act</strong></p><p>This bill requires the National Telecommunications and Information Administration to carry out a campaign to educate the public on cybersecurity best practices. The campaign must provide information on identifying cybersecurity risks and encourage the public to take certain actions, such as changing default passwords and declining unnecessary privilege requests from mobile applications.</p>"
        },
        "title": "American Cybersecurity Literacy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2154.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Cybersecurity Literacy Act</strong></p><p>This bill requires the National Telecommunications and Information Administration to carry out a campaign to educate the public on cybersecurity best practices. The campaign must provide information on identifying cybersecurity risks and encourage the public to take certain actions, such as changing default passwords and declining unnecessary privilege requests from mobile applications.</p>",
      "updateDate": "2025-09-15",
      "versionCode": "id119hr2154"
    },
    "title": "American Cybersecurity Literacy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Cybersecurity Literacy Act</strong></p><p>This bill requires the National Telecommunications and Information Administration to carry out a campaign to educate the public on cybersecurity best practices. The campaign must provide information on identifying cybersecurity risks and encourage the public to take certain actions, such as changing default passwords and declining unnecessary privilege requests from mobile applications.</p>",
      "updateDate": "2025-09-15",
      "versionCode": "id119hr2154"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2154ih.xml"
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
      "title": "American Cybersecurity Literacy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Cybersecurity Literacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a cybersecurity literacy campaign, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:33:36Z"
    }
  ]
}
```
