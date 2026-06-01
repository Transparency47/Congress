# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4471?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4471
- Title: No More Narcos Act
- Congress: 119
- Bill type: HR
- Bill number: 4471
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-01-13T09:05:41Z
- Update date including text: 2026-01-13T09:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4471",
    "number": "4471",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "No More Narcos Act",
    "type": "HR",
    "updateDate": "2026-01-13T09:05:41Z",
    "updateDateIncludingText": "2026-01-13T09:05:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "AZ"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
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
      "sponsorshipDate": "2026-01-12",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4471ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4471\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Vasquez (for himself and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish and implement an informational campaign and national strategy to prevent minors from working with cartels and transnational criminal organizations.\n#### 1. Short title\nThis Act may be cited as the No More Narcos Act .\n#### 2. Informational campaign and national strategy\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Attorney General, acting through the Administrator of the Drug Enforcement Administration and in consultation with the Secretary of Homeland Security, the Secretary of Education, the Director of National Drug Control Policy, and such other Federal, State, local, or tribal agency as may be appropriate, shall establish and implement an informational campaign to educate covered students on the dangers and risks of working with cartels or other transnational criminal organizations.\n##### (b) National strategy\nThe Secretary of Homeland Security shall establish and implement a national strategy to combat cartels and other transnational criminal organizations targeting and recruiting minors in the United States to engage in unlawful smuggling or trafficking activities.\n##### (c) Definitions\nIn this Act:\n**(1) Covered student**\nThe term covered student means students in middle grades and high school in United States communities 100 miles or less from the United States-Mexico border.\n**(2) High school**\nThe term high school has the meaning given that term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(3) Middle grades**\nThe term middle grades has the meaning given that term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(4) Minor**\nThe term minor means an individual who has not attained 18 years of age.\n**(5) Transnational criminal organizations**\nThe term transnational criminal organization means self-perpetuating associations of individuals who\u2014\n**(A)**\noperate transnationally for the purpose of obtaining power, influence, monetary or commercial gains, wholly or in part by illegal means, while protecting their illegal activities through\u2014\n**(i)**\na pattern of corruption or violence; or\n**(ii)**\na transnational organizational structure and the exploitation of transnational commerce or communication mechanisms. Transnational criminal organizations; and\n**(B)**\nengage in a broad range of criminal activities, including drug and weapons trafficking, migrant smuggling, human trafficking, cybercrime, intellectual property theft, money laundering, wildlife and timber trafficking, illegal fishing, and illegal mining.\n#### 3. DOJ Assets Forfeiture Fund\nSection 524(c)(1) of title 28, United States Code, is amended\u2014\n**(1)**\nin subparagraph (I), by striking and at the end;\n**(2)**\nin subparagraph (J)(ii), by striking the period and inserting ; and ; and\n**(3)**\nby inserting after subparagraph (J) the following:\n(K) payments for\u2014 (i) the informational campaign to educate students on the dangers and risks of working with cartels or other transnational criminal organizations under the No More Narcos Act; and (ii) the national strategy to combat cartels and other transnational criminal organizations targeting and recruiting minors in the United States to engage in unlawful smuggling or trafficking activities under such Act. .",
      "versionDate": "2025-07-16",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-11T15:24:37Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4471ih.xml"
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
      "title": "No More Narcos Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-29T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No More Narcos Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T04:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish and implement an informational campaign and national strategy to prevent minors from working with cartels and transnational criminal organizations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-29T04:03:15Z"
    }
  ]
}
```
