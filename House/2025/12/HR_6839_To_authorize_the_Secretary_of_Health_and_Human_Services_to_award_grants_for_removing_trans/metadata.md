# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6839?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6839
- Title: Vaccine Transportation Access Act
- Congress: 119
- Bill type: HR
- Bill number: 6839
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-01-21T09:05:24Z
- Update date including text: 2026-01-21T09:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6839",
    "number": "6839",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001300",
        "district": "44",
        "firstName": "Nanette",
        "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
        "lastName": "Barrag\u00e1n",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Vaccine Transportation Access Act",
    "type": "HR",
    "updateDate": "2026-01-21T09:05:24Z",
    "updateDateIncludingText": "2026-01-21T09:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:07:15Z",
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IN"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "TN"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-18",
      "state": "DC"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "TX"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "GA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "WA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6839ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6839\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Ms. Barrag\u00e1n (for herself, Mr. Carson , Mr. Cohen , Mrs. Dingell , Mr. Garc\u00eda of Illinois , Mr. Goldman of New York , Ms. Norton , Mr. Soto , Mr. Tonko , and Mr. Veasey ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize the Secretary of Health and Human Services to award grants for removing transportation barriers to accessing eligible vaccines for individuals from low-income communities, minority communities, or other communities in which transportation poses a barrier to health care access, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Vaccine Transportation Access Act .\n#### 2. Grant program for vaccine access and mobility\n##### (a) General authority\n**(1) Awards**\nThe Secretary shall award grants to qualified community organizations to assist in financing projects to remove transportation barriers to accessing eligible vaccines for individuals from low-income communities, minority communities, or other communities in which transportation poses a barrier to health care access.\n**(2) Transfer of duties**\nThe Secretary shall\u2014\n**(A)**\nenter into agreements with State health agencies for purposes of carrying out the duties assigned to the Secretary under this section; and\n**(B)**\ntransfer to such agencies for such purposes funds appropriated to carry out this section.\n##### (b) Application\nA qualified community organization seeking a grant under this section shall submit to the Secretary an application that contains\u2014\n**(1)**\na description of the project to be funded through the grant;\n**(2)**\nan identification of all project partners and their specific role in the proposed project, including private for-profit and nonprofit entities engaged in the coordination of transportation services for the project; and\n**(3)**\nspecific performance measures the qualified community organization will use to reduce cancellations or missed appointments.\n##### (c) Period of performance\nEach grant awarded under subsection (a) shall be for a period of performance of not less than 6 months.\n##### (d) Use of funds\nEach grant awarded under subsection (a)\u2014\n**(1)**\nshall be used to develop, expand, and enhance access to transportation to and from sites for receipt of an eligible vaccine by individuals from low-income communities, minority communities, or other communities in which transportation poses a barrier to health care access; and\n**(2)**\nmay be used to\u2014\n**(A)**\nprovide prescheduled or on-demand transportation to and from a site for administration of an eligible vaccine; or\n**(B)**\nprovide first and last mile transportation services for appointments for administration of such a vaccine.\n##### (e) Reporting\n**(1) Grant recipients**\nAs a condition on receipt of a grant under this section, a grantee shall agree to submit to the Secretary, not later than 6 months after the completion of the period of performance of the grant, a report containing such information as the Secretary determines necessary to evaluate performance under the grant.\n**(2) Annual report to Congress**\nNot later than one year after the date of enactment of this Act, and annually thereafter during the term of the grant program under this section, the Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate a report containing a summary of the information received by the Secretary during the preceding year under paragraph (1).\n##### (f) Definitions\nFor purposes of this section:\n**(1) Eligible vaccine**\nThe term eligible vaccine means any immunization that\u2014\n**(A)**\nhad in effect a recommendation from the Advisory Committee on Immunization Practices of the Centers for Disease Control and Prevention with respect to the individual involved as of October 25, 2024, including such an immunization as updated or changed after that date under a supplement to a biologics license application approved by the Food and Drug Administration; or\n**(B)**\nis recommended under evidenced-based, clinical care guidelines published by one or more United States professional medical societies.\n**(2) First and last mile**\nThe term first and last mile means, with respect to transportation services and an individual\u2019s trip to and from a vaccine appointment\u2014\n**(A)**\ntransportation\u2014\n**(i)**\nbetween the individual\u2019s point of trip origin and a source of public transit; and\n**(ii)**\nbetween a source of public transit and the individual\u2019s destination; or\n**(B)**\nwhere no source of public transit is available, transportation between the individual\u2019s point of trip origin and the individual\u2019s destination.\n**(3) Qualified community organization**\nThe term qualified community organization means an organization that\u2014\n**(A)**\nis a nonprofit organization; and\n**(B)**\nhas experience in\u2014\n**(i)**\nmanaging Federal grants; and\n**(ii)**\nproviding services to low-income or minority communities or communities that disproportionately experience disparities in health status and health care access.\n**(4) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n##### (g) Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this section.\n#### 3. Federal medical assistance percentage\nSection 1905(b) of the Social Security Act ( 42 U.S.C. 1396d(b) ) is amended by adding at the end the following new sentence: Notwithstanding the first sentence of this subsection, the Federal medical assistance percentage shall be 100 per centum with respect to amounts expended for nonemergency transportation benefits provided to individuals eligible for medical assistance under this subchapter that are attributable to transportation costs incurred on or after the date of the enactment of this sentence related to providing eligible vaccines (as defined in section 2(f) of the Vaccine Transportation Access Act) to such individuals under the State plan. .",
      "versionDate": "2025-12-18",
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
        "name": "Health",
        "updateDate": "2026-01-20T15:03:58Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6839ih.xml"
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
      "title": "Vaccine Transportation Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Vaccine Transportation Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Health and Human Services to award grants for removing transportation barriers to accessing eligible vaccines for individuals from low-income communities, minority communities, or other communities in which transportation poses a barrier to health care access, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T05:48:17Z"
    }
  ]
}
```
