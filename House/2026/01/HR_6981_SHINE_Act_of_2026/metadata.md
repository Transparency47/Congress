# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6981?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6981
- Title: SHINE Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6981
- Origin chamber: House
- Introduced date: 2026-01-08
- Update date: 2026-05-06T21:30:27Z
- Update date including text: 2026-05-06T21:30:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-08: Introduced in House

## Actions

- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6981",
    "number": "6981",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000590",
        "district": "3",
        "firstName": "Susie",
        "fullName": "Rep. Lee, Susie [D-NV-3]",
        "lastName": "Lee",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "SHINE Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-06T21:30:27Z",
    "updateDateIncludingText": "2026-05-06T21:30:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-08",
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
      "actionDate": "2026-01-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T15:00:10Z",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "AZ"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6981ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6981\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 8, 2026 Ms. Lee of Nevada (for herself, Mr. Ciscomani , Mr. Tonko , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Energy to further develop and support the adoption of a voluntary streamlined permitting and inspection process for authorities having jurisdiction over the permitting of qualifying distributed energy systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlining Home Installation of New Energies Act of 2026 or the SHINE Act of 2026 .\n#### 2. Establishment of program to facilitate voluntary streamlined process for local permitting of qualifying distributed energy systems\n##### (a) Definitions\nIn this section:\n**(1) Authority having jurisdiction**\nThe term authority having jurisdiction means any State, county, local, or Tribal office or official with jurisdiction\u2014\n**(A)**\nto issue permits relating to qualifying distributed energy systems;\n**(B)**\nto conduct inspections to enforce the requirements of a relevant code or standard relating to qualifying distributed energy systems; or\n**(C)**\nto approve the installation of, or the equipment and materials used in the installation of, qualifying distributed energy systems.\n**(2) Qualifying distributed energy system**\nThe term qualifying distributed energy system means any equipment or materials installed in, on, or near a residential building to support onsite or local energy use, including\u2014\n**(A)**\nto generate electricity from distributed renewable energy sources, including from\u2014\n**(i)**\nsolar photovoltaic systems or similar solar energy technologies; and\n**(ii)**\nwind power systems;\n**(B)**\nto store and discharge electricity from batteries with a capacity of at least 2 kilowatt hours;\n**(C)**\nto charge a plug-in electric drive vehicle at a power rate of at least 2 kilowatts; or\n**(D)**\nto refuel a hydrogen fuel cell electric vehicle.\n**(3) Secretary**\nThe term Secretary means the Secretary of Energy.\n##### (b) Program\nNot later than 180 days after the date of enactment of this Act, the Secretary, in consultation with trade associations and other entities representing distributed energy system installers and organizations representing State, local, and Tribal governments engaged in permitting, shall carry out a program to further develop, expand, and support the adoption of a voluntary streamlined permitting and inspection process for authorities having jurisdiction to use for the permitting of qualifying distributed energy systems.\n##### (c) Activities of the program\nIn carrying out the program established under subsection (b), the Secretary shall\u2014\n**(1)**\nfurther develop and expand an exemplary streamlined permitting process that includes an online permitting platform\u2014\n**(A)**\nfor expediting, standardizing, and streamlining permitting; and\n**(B)**\nthat authorities having jurisdiction may voluntarily use to receive, review, and approve permit applications relating to qualifying distributed energy systems;\n**(2)**\nestablish targets for the adoption of a streamlined, expedited permitting process by authorities having jurisdiction;\n**(3)**\nprovide technical assistance and training directly or indirectly to authorities having jurisdiction on using and adopting the exemplary streamlined permitting process described in paragraph (1), including the adoption of any necessary building codes;\n**(4)**\ndevelop a voluntary inspection protocol and related tools to expedite, standardize, and streamline the inspection of qualifying distributed energy systems, including\u2014\n**(A)**\nby investigating the potential for using remote inspections;\n**(B)**\nby investigating the potential for sample-based inspection for distributed energy system installers with a demonstrated track record of high-quality work; and\n**(C)**\nby investigating opportunities to integrate the voluntary inspection protocol into the online permitting platform described in paragraph (1) and the platforms of government software providers; and\n**(5)**\ntake any other action to expedite, standardize, streamline, or improve the process for permitting, inspecting, or interconnecting qualifying distributed energy systems.\n##### (d) Support services\nThe Secretary shall\u2014\n**(1)**\nsupport the provision of technical assistance to authorities having jurisdiction, any administrator of the online permitting platform described in subsection (c)(1), government software providers, and any other entity determined appropriate by the Secretary in carrying out the activities described in subsection (c); and\n**(2)**\nprovide such financial assistance as the Secretary determines appropriate from any funds appropriated to carry out this section.\n##### (e) Authority having jurisdiction certification program\n**(1) In general**\nThe Secretary may certify authorities having jurisdiction that implement the exemplary streamlined permitting process described in subsection (c)(1).\n**(2) Process**\nThe Secretary may confer a certification under paragraph (1) through existing programs within the Department of Energy.\n**(3) Prizes**\nThe Secretary may award prizes to authorities having jurisdiction, using funds appropriated to the Secretary to carry out this section, to encourage authorities having jurisdiction to adopt the exemplary streamlined permitting process or the voluntary inspection protocol established under paragraphs (1) and (4) of subsection (c), respectively.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $20,000,000 for each of fiscal years 2027 through 2030.",
      "versionDate": "2026-01-08",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-18",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Agriculture, Ways and Means, Natural Resources, Financial Services, Transportation and Infrastructure, Education and Workforce, Oversight and Government Reform, and Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7977",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Energy Bills Relief Act",
      "type": "HR"
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
        "updateDate": "2026-01-12T16:54:32Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6981ih.xml"
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
      "title": "SHINE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T09:24:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHINE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T09:24:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamlining Home Installation of New Energies Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T09:24:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Energy to further develop and support the adoption of a voluntary streamlined permitting and inspection process for authorities having jurisdiction over the permitting of qualifying distributed energy systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T09:18:17Z"
    }
  ]
}
```
