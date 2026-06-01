# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8146?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8146
- Title: Rural Utilities Service Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 8146
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-04-21T02:38:03Z
- Update date including text: 2026-04-21T02:38:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-03-27: Introduced in House

## Actions

- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8146",
    "number": "8146",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001232",
        "district": "6",
        "firstName": "April",
        "fullName": "Rep. McClain Delaney, April [D-MD-6]",
        "lastName": "McClain Delaney",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Rural Utilities Service Modernization Act",
    "type": "HR",
    "updateDate": "2026-04-21T02:38:03Z",
    "updateDateIncludingText": "2026-04-21T02:38:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
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
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-27",
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
          "date": "2026-03-28T01:31:15Z",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "PA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8146ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8146\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Mrs. McClain Delaney (for herself and Mr. Bresnahan ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require the Secretary of Agriculture to establish a web-based platform to enable recipients of Federal financial assistance administered by the Rural Utilities Service to track the status of their projects throughout the permitting and review process, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Utilities Service Modernization Act .\n#### 2. Establishment of web-based platform to enable recipients of Federal financial assistance administered by the Rural Utilities Service to track the status of their projects throughout the permitting and review process\n##### (a) In general\nThe Secretary of Agriculture, through the Rural Utilities Service, shall establish, operate, and maintain a secure, web-based platform that is designed to improve predictability and accountability for recipients of Federal financial assistance administered by the Rural Utilities Service, by enabling the recipients to track the status of their projects throughout the permitting and review process (including environmental and interagency coordination).\n##### (b) Requirements\nIn carrying out subsection (a), the Secretary shall\u2014\n**(1)**\nrequire the Rural Utilities Service to determine, establish, and implement user access mechanisms enabling the recipients to view permitting and review status for their projects;\n**(2)**\nrequire clear status indicators and estimated timelines for each phase of the permitting and review process for projects assisted by the Rural Utilities Service;\n**(3)**\nensure that, through the platform, documents may be uploaded and downloaded and applicants may correspond with relevant Rural Utilities Service offices;\n**(4)**\nensure that automated notifications are provided to recipients when a project advances to a new review stage or when additional information or action is required; and\n**(5)**\ndirect the Rural Utilities Service to coordinate, as appropriate, with\u2014\n**(A)**\nother agencies of the Department of Agriculture;\n**(B)**\nthe Department of Commerce;\n**(C)**\nthe Department of Defense;\n**(D)**\nthe Department of Energy;\n**(E)**\nthe Department of the Interior;\n**(F)**\nthe Department of Transportation;\n**(G)**\nthe General Services Administration;\n**(H)**\nthe U.S. Army Corps of Engineers; and\n**(I)**\nany relevant Federal permitting authorities,\nincluding environmental reviews conducted pursuant to the National Environmental Policy Act and the National Historic Preservation Act, while maintaining the responsibility of the Rural Utilities Service for project status reporting.\n##### (c) Annual reports\nWithin 2 years after the date of the enactment of this Act, and annually thereafter, the Secretary of Agriculture shall submit to Congress a written report that describes the development, implementation, use, and performance of the platform.\n##### (d) Limitations on authorization of appropriations\n**(1) In general**\nTo carry out this section, there are authorized to be appropriated to the Secretary of Agriculture a total of not more than $30,000,000, of which\u2014\n**(A)**\na total of not less than $20,000,000 and not more than $24,000,000 shall be available for fiscal years 2026 and 2027 for development of the platform; and\n**(B)**\na total of not less than $6,000,000 and not more than $10,000,000 shall be available for each of fiscal years 2028 through 2035 for operation and maintenance of the platform.\n**(2) Availability**\nThe amounts made available by paragraph (1) are authorized to remain available until expended.\n#### 3. Rural Utilities Service preplanning education and planning grants\n##### (a) In general\nThe Secretary of Agriculture, acting through the Administrator of the Rural Utilities Service (in this section referred to as the Secretary), shall make grants to eligible entities for predevelopment planning, permitting, and early-stage project preparation activities under any program administered by the Rural Utilities Service.\n##### (b) Eligible entities\nAn entity is eligible for a grant under this section if the entity is qualified to participate in a program administered by the Rural Utilities Service and is unable to finance predevelopment work by borrowing or other means.\n##### (c) Cost-Sharing\nThe amount of each grant under this section shall be not more than 75 percent of the cost of the activities for which the grant is made.\n##### (d) Use of funds\nThe recipient of a grant under this section shall use the grant for pre-development activities such as\u2014\n**(1)**\nfeasibility studies, permitting, design assistance, and other pre-development planning activities;\n**(2)**\ntechnical assistance and training to improve planning and readiness for a program administered by the Rural Utilities Service; or\n**(3)**\nparticipation in a partnerships with a Federal, State, Tribal, or local entity to support project preparation.\n##### (e) Prohibition\nA grant under this section shall not be used to reimburse costs of work completed before the grant is made.\n##### (f) Administrative provisions\n**(1) Guidelines**\nThe Secretary shall issue guidelines relating to applications for grants under this section, selection of grantees, and administration of the grants.\n**(2) Limitation on administrative costs**\nIn administering this section, the Secretary shall limit administrative costs incurred pursuant to this section, to ensure that funds made available to carry out this section are used for predevelopment activities to the maximum extent practicable.\n##### (g) Reports\nThe recipient of a grant under this section shall transmit annual reports to the Secretary on the activities funded with the grant and the outcomes of the activities.\n##### (h) Limitations on authorization of appropriations\nTo carry out this section, there are authorized to be appropriated not more than $15,000,000 for each of fiscal years 2026 through 2035.\n#### 4. Notice of funding opportunity timelines\n##### (a) Issuance of regulations\nWithin 6 months after the date of the enactment of this Act, the Secretary of Agriculture, acting through Rural Development and the Administrator of the Rural Utilities Service, shall prescribe final regulations to improve timelines for notices of funding opportunity for grants administered by the Rural Utilities Service, that should provide for\u2014\n**(1)**\na uniform notice of funding opportunity timeline applicable to all Rural Utilities Service grant programs;\n**(2)**\nsector-specific notice of funding opportunity timelines for major program areas of the Rural Utilities Service, including\u2014\n**(A)**\nelectricity;\n**(B)**\ntelecommunications, including telephone and broadband;\n**(C)**\nbroadband distance learning and telemedicine; and\n**(D)**\nwater and waste disposal; or\n**(3)**\nif the approaches described in paragraphs (1) and (2) are not practicable, an alternative approach to improving predictability and coordination of notice of funding opportunity timelines.\n##### (b) Implementation\nThe Secretary shall implement the final regulations within 18 months after the date of the enactment of this Act.\n#### 5. Online grant applications\nWithin 2 years after the date of the enactment of this Act, the Administrator of the Rural Utilities Service shall require all applications for a grant administered by the Rural Utilities Service to be submitted electronically through an online system or, if such an applicant is unable to so submit such an application, provide alternative means for the applicant to submit the application.\n#### 6. Staff assessment and report to Congress\n##### (a) Staff assessment\nThe Secretary of Agriculture shall evaluate the processes used by the staff of the Rural Utilities Service to\u2014\n**(1)**\nreview applications for assistance from programs administered by the Rural Utilities Service;\n**(2)**\nprovide related technical assistance; and\n**(3)**\nmonitor assistance awardees,\nwith the goal of maximizing the efficiency and effectiveness of the programs.\n##### (b) Report to Congress\n2 years after the date of the enactment of this Act, the Secretary of Agriculture and the Administrator of the Rural Utilities Service shall jointly prepare and submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report that\u2014\n**(1)**\nexamines, at a minimum\u2014\n**(A)**\nthe workload of the staff of the Rural Utilities Service, the allocation of the workload, and the efficiency of the staff in reviewing applications and assisting applicants for assistance under the programs administered by the Rural Utilities Service; and\n**(B)**\nthe timeliness, consistency, and quality of technical assistance provided and award decisions made under the programs; and\n**(2)**\nsets forth\u2014\n**(A)**\nrecommendations to enhance the effectiveness of the online permitting platform established under section 2;\n**(B)**\nan assessment of how permitting for projects assisted by the Rural Utilities Service could be expedited; and\n**(C)**\nfindings that could strengthen service delivery to rural communities.",
      "versionDate": "2026-03-27",
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
        "updateDate": "2026-04-21T02:38:03Z"
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
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8146ih.xml"
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
      "title": "Rural Utilities Service Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T05:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Utilities Service Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture to establish a web-based platform to enable recipients of Federal financial assistance administered by the Rural Utilities Service to track the status of their projects throughout the permitting and review process, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T05:18:52Z"
    }
  ]
}
```
