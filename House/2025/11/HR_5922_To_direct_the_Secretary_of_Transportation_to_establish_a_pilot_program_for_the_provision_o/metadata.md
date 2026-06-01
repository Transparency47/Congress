# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5922?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5922
- Title: Improving Accessibility Through Microtransit Act
- Congress: 119
- Bill type: HR
- Bill number: 5922
- Origin chamber: House
- Introduced date: 2025-11-04
- Update date: 2026-02-24T09:05:30Z
- Update date including text: 2026-02-24T09:05:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-04: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-05 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-11-04: Introduced in House

## Actions

- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-05 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5922",
    "number": "5922",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Improving Accessibility Through Microtransit Act",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:30Z",
    "updateDateIncludingText": "2026-02-24T09:05:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-05",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-04",
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
          "date": "2025-11-04T19:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-05T18:04:38Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "sponsorshipDate": "2025-11-04",
      "state": "PA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5922ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5922\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Mr. Stanton (for himself and Mr. Bresnahan ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to establish a pilot program for the provision of competitive grants to eligible entities for use improving the availability of accessible microtransit services to individuals with disabilities or mobility impairments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Accessibility Through Microtransit Act .\n#### 2. Pilot program for provision of grants to improve microtransit services\n##### (a) Pilot program\nNot later than 180 days after the date of enactment of this Act, the Secretary of Transportation, acting through the Administrator of the Federal Transit Administration, shall establish a pilot program (herein referred to as the Pilot Program ) under which the Secretary may make grants, on a competitive basis, to covered entities for use improving the availability of microtransit services to individuals with disabilities or mobility impairments, including individuals who use a wheelchair.\n##### (b) Eligibility\n**(1) In general**\nTo be eligible to receive a grant under the Pilot Program, a covered entity must submit an application at such time and in such manner as the Secretary may require, and that includes the following information:\n**(A)**\nA description of the types of disabilities or mobility impairments of individuals the covered entity expects to provide with microtransit services through the expenditure of grant funds.\n**(B)**\nThe approximate square miles of the geographic area in which the covered entity expects to provide microtransit services through the expenditure of grant funds.\n**(C)**\nAny additional information as the Secretary may require.\n**(2) Public-private partnership**\nA covered entity may submit an application on behalf of a partnership between a covered entity and a private entity for the provision of a microtransit service.\n##### (c) Selection\n**(1) Criteria**\nIn selecting applicants to receive a grant under the Pilot Program, the Secretary shall select a covered entity based on criteria established by the Secretary.\n**(2) Priority**\nThe Secretary shall prioritize for receipt of a grant under the Pilot Program applicants\u2014\n**(A)**\nwhose applications demonstrate how each microtransit service intended to be acquired or provided using grant funds will\u2014\n**(i)**\nprovide greater accessibility for individuals with disabilities or mobility impairments;\n**(ii)**\naddress a lack of accessible service in the geographic area in which the covered entity expects to provide microtransit services through the expenditure of grant funds; and\n**(iii)**\ndeliver economic benefits in such geographic area, such as improving access to jobs or promoting local economic development through enhanced mobility; and\n**(B)**\nthat intend to use grant funds to\u2014\n**(i)**\nprovide wheelchair accessible vehicles and accessible mobile applications for use in microtransit services;\n**(ii)**\nenable low-income individuals, including individuals without access to smartphone technology or a credit card, to access any transportation services made available through the project;\n**(iii)**\ncarry out an allowable use described in subsection (e) that improves the performance of the transit and microtransit services system of the applicant;\n**(iv)**\naccelerate the deployment of advanced transit technologies, including shared-use mobility services;\n**(v)**\nimprove safety within the area serviced by the applicant; or\n**(vi)**\ndirectly hire workers to perform microtransit services within the system of the applicant.\n##### (d) Grant amount limitation\nIn carrying out the Pilot Program, the Secretary may not issue a grant for an amount greater than $3,000,000.\n##### (e) Allowable uses\nA recipient of a grant under the Pilot Program may use grant funds for the following uses:\n**(1)**\nTo purchase or lease a covered vehicle for use in a microtransit service existing as of the date on which the recipient submits an application in accordance with subsection (b).\n**(2)**\nTo fund initial training for individuals to be able to drive a covered vehicle operating in a mircotransit service of the recipient.\n**(3)**\nTo fund continuing education training for drivers of a covered vehicle operating in a microtransit service of the recipient.\n**(4)**\nTo contract for the provision of activities necessary for the provisions of a microtransit service, including capital management and operations-related activities.\n**(5)**\nTo acquire software or license technology that facilitates microtransit services.\n**(6)**\nAny other uses determined by the Secretary to improve the accessibility or availability of microtransit services for individuals with disabilities or mobility impairments.\n##### (f) Camera system requirement\n**(1) Stipulation**\nAs a condition of receiving funds under the Pilot Program, each recipient shall agree to install, if necessary, and maintain on each vehicle of the microtransit service of the recipient an interior camera system\u2014\n**(A)**\ncapable of recording passengers and drivers on the vehicle; and\n**(B)**\nthat may\u2014\n**(i)**\ncontinuously record video and audio while the vehicle is engaged in passenger service;\n**(ii)**\nbe tamper-resistant;\n**(iii)**\nretain recordings for 30 days or more; and\n**(iv)**\nproduce recordings in a format accessible to the recipient and, upon lawful request, law enforcement.\n**(2) Recording access limitations**\nA recording produced by an interior camera system maintained pursuant to paragraph (1) may not be released to the public and access to the recording shall be limited to\u2014\n**(A)**\nemployees of the recipient who the recipient authorizes to access; and\n**(B)**\nlaw enforcement pursuant to a lawful request.\n##### (g) Labor standards\nThe Secretary shall apply the requirements of section 5333 of title 49, United States Code, to projects financed with Pilot Program grant funds.\n##### (h) Termination\nThe authority to carry out the Pilot Program under this section shall terminate on the date that is 5 years after the date on which the Pilot Program commences.\n##### (i) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary $20,000,000 to carry out this section. Such amount is authorized to remain available through the fiscal year in which the Pilot Program is terminated pursuant to subsection (f).\n##### (j) Definitions\nIn this section:\n**(1) Covered entity**\nThe term covered entity means\u2014\n**(A)**\na State government;\n**(B)**\na local government;\n**(C)**\na Tribal organization; or\n**(D)**\na metropolitan planning organization.\n**(2) Covered vehicle**\nThe term covered vehicle means a multi-passenger vehicle that, to be accessible to individuals with disabilities or mobility impairments (including individuals who use a wheelchair), is equipped with handicap accessible designs, including\u2014\n**(A)**\na ramp;\n**(B)**\na hydraulic mechanism designed to load and unload a wheelchair; and\n**(C)**\nany other handicap accessible designs determined appropriate by the Secretary.\n**(3) Fixed route system**\nThe term fixed route system has the meaning given such term in section 221 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12141 ).\n**(4) Microtransit service**\nThe term microtransit service means a technology-enabled, on-demand service with dynamically generated routing that uses a managed fleet of multi-passenger vehicles dedicated to that service.\n**(5) On-demand service**\nWith respect to a microtransit service, the term on-demand service includes the following:\n**(A)**\nA service to connect an individual from a starting point to a fixed route system or from a fixed route system to a destination of the individual.\n**(B)**\nA hub-to-hub zone-based service.\n**(C)**\nA service that is a commingling of a general transit service and a paratransit or other special transportation service provided in accordance with section 223 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12143 ).\n**(D)**\nA point-to-point service within a specific zone or limited geographic area.\n**(E)**\nAny other similar service, as determined by the Secretary of Transportation.\n**(6) Tribal organization**\nThe term Tribal organization has the meaning given such term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).",
      "versionDate": "2025-11-04",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-25T16:41:01Z"
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
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5922ih.xml"
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
      "title": "Improving Accessibility Through Microtransit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Accessibility Through Microtransit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to establish a pilot program for the provision of competitive grants to eligible entities for use improving the availability of accessible microtransit services to individuals with disabilities or mobility impairments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T12:18:14Z"
    }
  ]
}
```
