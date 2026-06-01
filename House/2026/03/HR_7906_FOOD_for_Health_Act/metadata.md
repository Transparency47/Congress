# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7906?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7906
- Title: FOOD for Health Act
- Congress: 119
- Bill type: HR
- Bill number: 7906
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-05-01T21:41:23Z
- Update date including text: 2026-05-01T21:41:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-12 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-12 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7906",
    "number": "7906",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "K000385",
        "district": "2",
        "firstName": "Robin",
        "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
        "lastName": "Kelly",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "FOOD for Health Act",
    "type": "HR",
    "updateDate": "2026-05-01T21:41:23Z",
    "updateDateIncludingText": "2026-05-01T21:41:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:30:10Z",
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
          "date": "2026-03-12T13:30:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "VA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "DC"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "AL"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "IL"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "AL"
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
      "sponsorshipDate": "2026-03-12",
      "state": "OR"
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
      "sponsorshipDate": "2026-03-17",
      "state": "PA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7906ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7906\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Ms. Kelly of Illinois (for herself, Mrs. Kiggans of Virginia , Ms. Norton , Ms. Sewell , Mr. Davis of Illinois , Mr. Figures , and Ms. Bynum ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Agriculture to establish and administer a pilot program to provide grants to support Food is Medicine programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fueling Optimal Outcomes through Diet for Health Act or the FOOD for Health Act .\n#### 2. Food is Medicine pilot grant program\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Secretary shall establish and administer a pilot program to award grants, on a competitive basis, to eligible entities described in subsection (b) to support Food is Medicine programs.\n##### (b) Application\nTo be eligible for a grant under this section, an entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary determines is appropriate.\n##### (c) Use of funds\nA grant awarded under this section may only be used to support the activities of a Food is Medicine program, including\u2014\n**(1)**\noperating an on-site emergency feeding operation;\n**(2)**\nmedically tailored packaging or delivery of groceries;\n**(3)**\nmedically tailored meals and produce prescriptions;\n**(4)**\nproviding individual or group-based evidence-based cooking skills (including through the use of digital technologies);\n**(5)**\npromoting dietary intervention strategies or other health-related strategies; and\n**(6)**\ntransportation of program participants to and from the communities served by the program.\n##### (d) Priority\nIn awarding grants under this section, the Secretary shall give priority to eligible entities described in subsection (b)\u2014\n**(1)**\nthat will incorporate local and regional foods, as determined by the Secretary, into activities funded by the grant; or\n**(2)**\nthat will include registered dieticians or nutrition professionals in the activities funded by the grant.\n##### (e) Regional balance; advancing health outcomes\nIn awarding grants under this section, the Secretary shall, to the maximum extent practicable\u2014\n**(1)**\nensure geographic diversity;\n**(2)**\nensure the equitable treatment of\u2014\n**(A)**\nurban, rural, and tribal communities; and\n**(B)**\ncommunities in territories of the United States; and\n**(3)**\nadvance health outcomes.\n##### (f) Reports\n**(1) In general**\n**(A) Initial report**\nNot later than 2 years after the date of the establishment of the pilot program referred to in subsection (a), the Secretary shall submit to Congress a report that\u2014\n**(i)**\nanalyzes the efficiency of such pilot program; and\n**(ii)**\nassesses the effect of such pilot program on patient outcomes and system costs.\n**(B) Final report**\nNot later than 6 years after the date of the establishment of the pilot program referred to in subsection (a), the Secretary shall submit to Congress an updated version of the report referred to in subparagraph (A).\n**(2) Elements**\nThe reports described in paragraph (1) shall each contain descriptions of\u2014\n**(A)**\nthe details and implementation of the pilot program referred to in subsection (a);\n**(B)**\nthe participant selection criteria used by Food is Medicine programs supported by grants awarded under this section;\n**(C)**\nthe diseases and other medical issues being addressed by grants awarded under this section;\n**(D)**\nthe strategies of such Food is Medicine programs in providing healthy, affordable food to program participants;\n**(E)**\nthe use and impact of medical nutrition therapy in coordination with the provision of food on the outcomes of participants treated by such Food is Medicine programs; and\n**(F)**\nthe impact of grants awarded under this section on the health (including behavioral health) of participants in such Food is Medicine programs.\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $20,000,000 for the period of fiscal years 2027 through 2031.\n##### (h) Definitions\nIn this section:\n**(1)**\nThe term diet-related disease means\u2014\n**(A)**\ndiabetes and prediabetes;\n**(B)**\na renal disease;\n**(C)**\nobesity (as defined by the Centers for Disease Control and Prevention or as otherwise defined by the Secretary);\n**(D)**\nhypertension;\n**(E)**\ndyslipidemia;\n**(F)**\nmalnutrition;\n**(G)**\nan eating disorder;\n**(H)**\ncancer;\n**(I)**\na gastrointestinal disease, including celiac disease;\n**(J)**\nHIV/AIDS;\n**(K)**\ncardiovascular disease;\n**(L)**\nmental illness, including depression and anxiety; and\n**(M)**\nany other disease as determined appropriate by the Secretary.\n**(2)**\nThe term Food is Medicine program means a program developed or operated by a community-based organization (such as an emergency feeding operation), in partnership with a health care provider (such as a community health clinic), to deploy the provision of food or medical nutrition therapy services to benefit participants experiencing, at risk of, or recovering from a diet-related disease.\n**(3)**\nThe term Secretary means the Secretary of Agriculture, in coordination with the Secretary of Health and Human Services.",
      "versionDate": "2026-03-12",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-01T20:14:24Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7906ih.xml"
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
      "title": "FOOD for Health Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FOOD for Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fueling Optimal Outcomes through Diet for Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture to establish and administer a pilot program to provide grants to support Food is Medicine programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T05:18:35Z"
    }
  ]
}
```
