# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5161?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5161
- Title: To establish in the Executive Office of the President an Office of Young Americans, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5161
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2025-09-17T20:08:43Z
- Update date including text: 2025-09-17T20:08:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5161",
    "number": "5161",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001200",
        "district": "9",
        "firstName": "Darren",
        "fullName": "Rep. Soto, Darren [D-FL-9]",
        "lastName": "Soto",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "To establish in the Executive Office of the President an Office of Young Americans, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-09-17T20:08:43Z",
    "updateDateIncludingText": "2025-09-17T20:08:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:03:05Z",
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
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "KY"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "OR"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "RI"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5161ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5161\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Mr. Soto (for himself, Mr. McGarvey , Ms. Bynum , Mr. Amo , and Ms. Pettersen ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo establish in the Executive Office of the President an Office of Young Americans, and for other purposes.\n#### 1. Office of Young Americans\n##### (a) In general\nThere is established in the Executive Office of the President an Office of Young Americans (referred to in this section as the Office ), which shall be headed by a Director (referred to in this section as the Director ).\n##### (b) Office leadership\n**(1) Appointments**\n**(A) In general**\nThe President shall appoint the Director and may appoint an Associate Director of the Office.\n**(B) Single Associate Director**\nThe President may not appoint an Associate Director to serve in the Office concurrently with another Associate Director.\n**(2) Functions of Director**\n**(A) Director**\nThe Director shall\u2014\n**(i)**\nidentify issues that primarily and substantially affect young Americans, including employment issues, education, mental health, housing, and climate change;\n**(ii)**\nadvise the President on\u2014\n**(I)**\nthe engagement and involvement of young Americans in the Federal Government; and\n**(II)**\nthe issues that primarily and substantially affect young Americans;\n**(iii)**\nsupport strategic coordination and communication between the Executive Office of the President and Federal agencies with respect to activities pertaining to issues primarily and substantially affecting young Americans;\n**(iv)**\nserve as the principal advisor to the President on all issues primarily and substantially affecting young Americans;\n**(v)**\nmake recommendations to the President regarding youth engagement in the Federal Government;\n**(vi)**\ncoordinate Federal activities to prepare for, and respond to, issues affecting young Americans and engagement in the Federal Government, by\u2014\n**(I)**\nproviding strategic direction to the heads of applicable Federal departments, agencies, and offices;\n**(II)**\nfacilitating coordination and communication between such Federal departments, agencies, and offices to improve youth engagement and involvement across all Federal departments; and\n**(III)**\nensuring that the authorities, capabilities, and expertise of each such department, agency, and office are appropriately leveraged to facilitate the whole-of-government response to issues related to young Americans;\n**(vii)**\nidentify opportunities to leverage current and emerging technologies, including through public-private partnerships, as appropriate, to address the future of the Nation\u2019s workforce through the development of skilled young Americans in these fields and advance the preparedness and response goals of the Federal Government;\n**(viii)**\nwork with relevant Federal officials to request funding through the President\u2019s Budgets and leverage programs of Federal Agencies to address the issues identified in the reports submitted under subparagraph (e); and\n**(ix)**\nperform such other functions and activities as prescribed by the President.\n**(B) Associate Director**\nThe Associate Director of the Office shall perform such functions as the Director may prescribe.\n**(3) Compensation**\n**(A) Director**\nThe annual rate of basic pay for the Director shall be the rate payable for level II of the Executive Schedule under section 5313 of title 5, United States Code.\n**(B) Associate Director**\nThe annual rate of basic pay for the Associate Director shall be the rate determined by the Director not exceeding the rate payable for level III of the Executive Schedule under section 5314 of title 5, United States Code.\n##### (c) Additional functions of the Director\nThe Director, in addition to the other duties and functions set forth in this section\u2014\n**(1)**\nshall\u2014\n**(A)**\nserve as a member of the Domestic Policy Council; and\n**(B)**\nseek to consult with State, Tribal, local, and territorial governments, industry, academia, professional societies, and other individuals and entities, as the Director deems appropriate, to identify issues that primarily and substantially affect young Americans; and\n**(2)**\nmay\u2014\n**(A)**\nuse for the administration of the Office, on a reimbursable basis, the available services, equipment, personnel, and facilities of Federal agencies; and\n**(B)**\nhold such hearings in various parts of the United States as the Director determines necessary to determine the views of the entities and individuals described in paragraph (1)(B) and of the general public concerning national needs and trends in\u2014\n**(i)**\nthe engagement and involvement of young Americans in the Federal Government; and\n**(ii)**\nissues that primarily and substantially affect young Americans.\n##### (d) Staffing and detailees\nIn carrying out functions under this section, the Director may\u2014\n**(1)**\nappoint individuals to not more than two full time equivalent positions in the Office;\n**(2)**\nfix the compensation of individuals appointed to such positions at a rate to be determined by the Director, up to the amount of annual compensation (excluding expenses) specified in section 102 of title 3, United States Code; and\n**(3)**\nuse the services of consultants, which may include by obtaining services described under section 3109(b) of title 5, United States Code, at rates not to exceed the rate of basic pay payable for level IV of the Executive Schedule under section 5315 of such title.\n##### (e) Preparedness outlook reports\nNot later than one year after the date of the enactment of this Act, and not less frequently than once every five years thereafter, the Director, in consultation with the heads of relevant Federal agencies and other officials within the Executive Office of the President, shall submit to the President, the Committees on Finance and on Health, Education, Labor, and Pensions of the Senate, and the Committees on Financial Services and on Education and the Workforce of the House of Representatives, and make publicly available, a report\u2014\n**(1)**\nidentifying and describing issues that warrant special attention from the President or the heads of such Federal agencies within the next 5 years regarding issues that primarily and substantially affect young Americans, including the effects of the policies, actions, and personnel of Federal agencies on the engagement and involvement of young Americans in the Federal Government; and\n**(2)**\nproviding recommendations and resource requirement for addressing the issues identified under paragraph (1).\n##### (f) Definitions\nIn this section:\n**(1) Federal agency**\nThe term Federal agency has the meaning given Executive agency in section 105 of title 5, United States Code.\n**(2) Young American**\nThe term young American means an individual who is a citizen or lawful permanent resident of the United States between the ages of 18 and 40 years old.",
      "versionDate": "2025-09-04",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-17T20:08:43Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5161ih.xml"
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
      "title": "To establish in the Executive Office of the President an Office of Young Americans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T08:18:23Z"
    },
    {
      "title": "To establish in the Executive Office of the President an Office of Young Americans, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-05T08:06:10Z"
    }
  ]
}
```
