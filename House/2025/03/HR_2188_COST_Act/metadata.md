# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2188?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2188
- Title: COST Act
- Congress: 119
- Bill type: HR
- Bill number: 2188
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-04-04T16:30:44Z
- Update date including text: 2025-04-04T16:30:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2188",
    "number": "2188",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "COST Act",
    "type": "HR",
    "updateDate": "2025-04-04T16:30:44Z",
    "updateDateIncludingText": "2025-04-04T16:30:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:08:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-18T16:07:50Z",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "MN"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2188ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2188\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Feenstra (for himself, Mr. Finstad , Mrs. Miller-Meeks , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Comptroller General of the United States to conduct an analysis of the costs of converting light-duty vehicles in the Federal fleet to electric vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Comparison of Sustainable Transportation Act or the COST Act .\n#### 2. Cost analysis of converting Federal fleet to electric vehicles\n##### (a) Cost analysis\nThe Comptroller General of the United States shall conduct\u2014\n**(1)**\nan analysis of the costs of replacing the light-duty vehicles in the Federal fleet that are fueled by gasoline with electric vehicles, including plug-in hybrid electric vehicles; and\n**(2)**\nan analysis of the costs of replacing the light-duty vehicles in the Federal fleet that are fueled by gasoline with flex-fuel ethanol vehicles.\n##### (b) Inclusions\nEach analysis conducted under subsection (a) shall include the costs necessary for deployment of infrastructure for each applicable type of electric vehicle or flex-fuel ethanol vehicle that it is feasible to be used in the Federal fleet nationwide.\n##### (c) Publication\nNot later than 1 year after the date of enactment of this Act, the Comptroller General shall publish online the cost analyses conducted under subsection (a).\n#### 3. Analysis of lifecycle emissions of E85 capable flex-fuel and electric vehicles\n##### (a) Analysis\nThe Secretary of Energy, utilizing the most recent Greenhouse gases, Regulated Emissions, and Energy use in Transportation model (commonly referred to as the \u201cGREET model\u201d) developed by Argonne National Laboratory, shall conduct a lifecycle analysis of greenhouse gas emissions from each of the following types of vehicles:\n**(1)**\nA conventional gasoline vehicle.\n**(2)**\nAn E85 capable flex-fuel vehicle.\n**(3)**\nA battery electric vehicle.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary of Energy shall submit to the Committee on Science, Space, and Technology of the House of Representatives, and the Committee on Commerce, Science, and Transportation of the Senate a report on the lifecycle analyses conducted under subsection (a).\n#### 4. Definitions\nIn this Act:\n**(1) E 85**\nThe term E85 means a fuel containing 85 percent ethanol and 15 percent gasoline.\n**(2) Federal fleet**\nThe term Federal fleet means the fleet of federally owned or operated motor vehicles as reported in the most recent Federal Fleet Report of the General Services Administration.\n**(3) Light-duty vehicle**\nThe term light-duty vehicle means a vehicle with a gross vehicle weight rating of less than or equal to 8,500 pounds.",
      "versionDate": "2025-03-18",
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
        "name": "Energy",
        "updateDate": "2025-04-04T16:30:44Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2188ih.xml"
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
      "title": "COST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Comparison of Sustainable Transportation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General of the United States to conduct an analysis of the costs of converting light-duty vehicles in the Federal fleet to electric vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:29Z"
    }
  ]
}
```
