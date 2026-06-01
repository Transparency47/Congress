# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7562?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7562
- Title: Office of Small Farms Establishment Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7562
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-03-09T22:51:51Z
- Update date including text: 2026-03-09T22:51:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7562",
    "number": "7562",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001159",
        "district": "10",
        "firstName": "Marilyn",
        "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
        "lastName": "Strickland",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Office of Small Farms Establishment Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-09T22:51:51Z",
    "updateDateIncludingText": "2026-03-09T22:51:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:02:20Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7562ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7562\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Ms. Strickland (for herself, Ms. Adams , and Mr. McGovern ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Department of Agriculture Reorganization Act of 1994 to establish an Office of Small Farms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Office of Small Farms Establishment Act of 2026 .\n#### 2. Office of Small Farms\n##### (a) In general\nSubtitle B of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6931 et seq. ) is amended by adding at the end the following:\n229. Office of small farms (a) Definitions In this section: (1) Small farm, ranch, or forest operation The term small farm, ranch, or forest operation means a farm, ranch, or forest operation that\u2014 (A) (i) is less than 180 acres; or (ii) meets another acreage-based definition of small , as determined by the Secretary, that takes into consideration\u2014 (I) the State or region in which the farm, ranch, or forest operation is located; (II) the production system of the farm, ranch, or forest operation; or (III) both; and (B) has an annual gross cash farm income of less than $350,000. (2) State office The term State office means\u2014 (A) a State office of\u2014 (i) the Farm Service Agency; (ii) the Natural Resources Conservation Service; or (iii) the rural development mission area; or (B) a regional office of the Risk Management Agency. (b) Establishment (1) In general The Secretary shall establish within the farm production and conservation mission area the Office of Small Farms. (2) Director (A) In general The Secretary shall appoint a Director of the Office of Small Farms (referred to in this section as the Director ). (B) Fpac A senior official within the farm production and conservation mission area may be appointed to serve as the Director. (c) Duties The Director shall\u2014 (1) coordinate efforts to improve support for small farms, ranches, and forest operations across all Department agencies and offices; (2) review Department programs and policies and identify statutory, regulatory, and administrative provisions, policies, and guidance that disadvantage small farm, ranch, or forest operation participation, and recommend changes to ensure that those programs and policies adequately serve small farms, ranches, and forest operations; (3) develop recommendations for new initiatives, including financing mechanisms and technical assistance opportunities, to specifically serve small farms, ranches, and forest operations relating to production, conservation, business planning, land access, and other issues, as determined by the Secretary; (4) make recommendations to Department agencies and offices and other Federal agencies on tracking small farm, ranch, or forest operation data, including demographics and program participation rates; (5) propose research agendas on topics that are of special interest to small farms, ranches, and forest operations; (6) provide or coordinate technical assistance through the Department or through cooperative agreements with other entities to operators of small farms, ranches, and forest operations to assist those operators\u2014 (A) to access the full complement of available Department grant, cost-share, and loan programs; (B) to implement activities using assistance received under those programs; and (C) with farmland preservation, including through succession planning; (7) implement a program directly or through cooperative agreements with other entities to provide grants of not more than $25,000 to operators of small farms, ranches, and forest operations for\u2014 (A) equipment and infrastructure repairs and upgrades; (B) uninsured losses; (C) business planning and market development assistance; (D) conservation practice adoption; (E) down payments for land acquisition; and (F) such other purposes as the Secretary determines to be appropriate; (8) operate a hotline through which operators of small farms, ranches, and forest operations can anonymously report problems that the operators encounter in attempts to access Department programs; (9) collaborate with other Federal and State agencies on how to effectively reach and serve small farms, ranches, and forest operations; and (10) determine whether to approve a plan submitted by a State small farms coordinator under subsection (e)(3)(A)(ii). (d) Liaisons (1) Appointment The following officials shall appoint, from among the officers and employees under the respective official, a liaison to the Office of Small Farms: (A) The Chief of the Natural Resources Conservation Service. (B) The Administrator of the Farm Service Agency. (C) The Administrator of the Risk Management Agency. (D) The Under Secretary of Agriculture for Rural Development. (E) The Director of the National Institute of Food and Agriculture. (F) The Administrator of the Agricultural Marketing Service. (G) The Administrator of the Economic Research Service. (H) The Administrator of the National Agricultural Statistics Service. (I) The Director of the Office of Partnerships and Public Engagement. (J) The heads of such other agencies, offices, and advisory groups as the Secretary determines to be appropriate, including\u2014 (i) the Office of Urban Agriculture and Innovative Production; and (ii) the Office of Tribal Relations. (2) Duties Each liaison appointed under paragraph (1) shall\u2014 (A) coordinate with the Office of Small Farms and the other liaisons appointed under that paragraph to develop and implement new strategies for outreach to and education for small farms, ranches, and forest operations; and (B) coordinate within the agency, office, mission area, or advisory group of the liaison on issues and outreach relating to small farms, ranches, and forest operations. (e) State small farms coordinators (1) In general (A) Designation (i) In general The Director, in consultation with State food and agriculture councils and directors of State offices, shall designate in each State a State small farms coordinator from among the employees of State offices. (ii) Employees The employee of a State office designated to be a State small farms coordinator may be the same employee designated to be the State beginning farmer and rancher coordinator under section 7404(c) of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 6934a(c) ). (B) Requirements To be designated as a State small farms coordinator, an employee shall\u2014 (i) be familiar with issues relating to small farms, ranches, and forest operations; and (ii) have the ability to coordinate with other Federal departments and agencies. (2) Training The Secretary shall develop a training plan to provide to each State small farms coordinator knowledge of programs and services available from the Department for small farms, ranches, and forest operations, taking into consideration the needs of all types of production methods. (3) Duties (A) In general A State small farms coordinator\u2014 (i) shall coordinate technical assistance at the State level to assist small farms, ranches, and forest operations in accessing programs of the Department; (ii) shall develop and submit to the Director for approval a State plan to improve the coordination, delivery, and efficacy of programs of the Department to small farms, ranches, and forest operations, taking into consideration the needs of all types of production methods, at each county and area office in the State; (iii) shall oversee implementation of an approved State plan described in clause (ii); (iv) may facilitate interagency and interdepartmental collaboration on issues relating to small farms, ranches, and forest operations at the State or regional level; (v) shall work with outreach coordinators in the State offices to ensure appropriate information about technical assistance is available at outreach events and activities; (vi) shall coordinate partnerships and joint outreach efforts with other organizations and government agencies serving small farms, ranches, and forest operations; and (vii) may provide grants under subsection (c)(7), in accordance with criteria established by the Director. (B) Individual duties Not less than 50 percent of the duties of an employee designated to be a State small farms coordinator shall be the duties described in subparagraph (A) or other duties relating to small farms, ranches, and forest operations. (f) Report to Congress Annually, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report describing\u2014 (1) the efforts of the Secretary to enhance participation by small farms, ranches, and forest operations in agricultural programs; and (2) the results achieved to enhance such participation for each such agricultural program. (g) Authorization of appropriations There are authorized to be appropriated\u2014 (1) $15,000,000 for each of fiscal years 2027 through 2031 for the administration of the Office of Small Farms; and (2) $10,000,000 for each of fiscal years 2027 through 2031 to provide technical assistance and grants authorized by this section. .\n##### (b) Technical amendment\nThe Department of Agriculture Reorganization Act of 1994 is amended by redesignating the first section 225 ( 7 U.S.C. 6925 ) (relating to the Food Access Liaison) as section 224A.\n##### (c) Conforming amendment\nSection 296(b) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 7014(b) ) is amended by adding at the end the following:\n(11) The authority of the Secretary to carry out section 229. .",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3860",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Office of Small Farms Establishment Act of 2026",
      "type": "S"
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
        "updateDate": "2026-03-09T22:51:51Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7562ih.xml"
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
      "title": "Office of Small Farms Establishment Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T08:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Office of Small Farms Establishment Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-06T08:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Department of Agriculture Reorganization Act of 1994 to establish an Office of Small Farms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-06T08:03:28Z"
    }
  ]
}
```
