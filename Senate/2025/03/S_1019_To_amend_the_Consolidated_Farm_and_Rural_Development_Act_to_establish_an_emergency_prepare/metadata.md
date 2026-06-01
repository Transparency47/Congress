# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1019?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1019
- Title: Rural Water System Disaster Preparedness and Assistance Act
- Congress: 119
- Bill type: S
- Bill number: 1019
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-10-31T11:03:14Z
- Update date including text: 2025-10-31T11:03:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1019",
    "number": "1019",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Rural Water System Disaster Preparedness and Assistance Act",
    "type": "S",
    "updateDate": "2025-10-31T11:03:14Z",
    "updateDateIncludingText": "2025-10-31T11:03:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
        "item": {
          "date": "2025-03-13T17:05:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "MS"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1019is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1019\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Ms. Cortez Masto (for herself and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to establish an emergency preparedness and response technical assistance program to assist entities that operate rural water or wastewater systems in preparing for and responding to natural or manmade disasters.\n#### 1. Short title\nThis Act may be cited as the Rural Water System Disaster Preparedness and Assistance Act .\n#### 2. Emergency preparedness and response technical assistance program\nSection 306(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a) ) is amended by adding at the end the following:\n(27) Emergency preparedness and response technical assistance program (A) In general The Secretary shall establish an emergency preparedness and response technical assistance program to provide grants to eligible entities to assist associations described in paragraph (1) that operate rural water or wastewater systems in preparing for and responding to natural or manmade disasters, as determined by the Secretary. (B) Eligible entities An entity eligible to receive a grant under subparagraph (A) is a nonprofit organization that\u2014 (i) has demonstrated experience providing emergency technical assistance for disaster preparation, recovery, and response activities to water and wastewater utilities nationwide; and (ii) has the capacity to deploy personnel that possess\u2014 (I) an active water or wastewater system operators\u2019 license; or (II) knowledge of water and wastewater utilities necessary to carry out activities described in subparagraph (C). (C) Eligible activities An eligible entity that receives a grant under subparagraph (A) shall use the grant\u2014 (i) to provide onsite personnel and equipment to assist with water and wastewater systems in the event of a disaster; (ii) to coordinate with statewide emergency response networks to assist with water and wastewater systems; (iii) to facilitate the development of disaster action plans between associations described in subparagraph (A), units of local government, the Federal Emergency Management Agency, and State emergency management agencies; (iv) to improve resiliency and mitigation planning with respect to water or wastewater systems; (v) to provide geographic information system mapping of water and wastewater systems; (vi) to prepare or update predisaster vulnerability assessments, emergency response plans, communication protocols, or hazard recognition and evaluation skills with respect to water and wastewater systems; (vii) to conduct preliminary damage assessments of critical infrastructure in the event of a disaster; (viii) to provide emergency services with respect to water and wastewater systems to restore service in the event of a disaster, including\u2014 (I) pump and motor evaluation and repair; (II) water disinfection and flushing; (III) leak detection; (IV) line repair; (V) water main and valve location; (VI) emergency power generation; (VII) bypass pumping; (VIII) water treatment; and (IX) maintaining safety measures; (ix) to address outstanding deficiencies focused on resolving health-based regulatory, operational, financial, and managerial deficiencies that impact the sustainability of water and wastewater systems; (x) to assist with application and reporting requirements for Federal and State agencies, including the Federal Emergency Management Agency and insurance recovery claims, with respect to water and wastewater systems; and (xi) to provide for disaster preparation, support, and response activities targeted to disadvantaged communities that lack the financial resources and human capital necessary to adequately address significant health, safety, or sanitary concerns with respect to the water and wastewater systems of those communities. (D) Use of funds (i) In general An eligible entity that receives a grant under subparagraph (A) may use the grant for salaries, supplies, and expenses relating to the activities described in subparagraph (C). (ii) Limitation Not more than 25 percent of the amount of a grant under subparagraph (A) may be used to purchase or reimburse the rental costs of appropriate emergency equipment, as determined by the Secretary. (E) Restriction An eligible entity that receives a grant under subparagraph (A) may not use the grant funds to pay for eligible activities for which the eligible entity receives other Federal funds. (F) Authorization of appropriations There is authorized to be appropriated to carry out this paragraph $20,000,000 for each of fiscal years 2025 through 2029. .",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
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
        "name": "Emergency Management",
        "updateDate": "2025-05-09T18:22:27Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1019is.xml"
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
      "title": "Rural Water System Disaster Preparedness and Assistance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Water System Disaster Preparedness and Assistance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consolidated Farm and Rural Development Act to establish an emergency preparedness and response technical assistance program to assist entities that operate rural water or wastewater systems in preparing for and responding to natural or manmade disasters.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T02:48:27Z"
    }
  ]
}
```
