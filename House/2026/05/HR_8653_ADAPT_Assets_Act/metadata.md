# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8653?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8653
- Title: ADAPT Assets Act
- Congress: 119
- Bill type: HR
- Bill number: 8653
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-30T08:05:51Z
- Update date including text: 2026-05-30T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-05-04: Introduced in House

## Actions

- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8653",
    "number": "8653",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000559",
        "district": "8",
        "firstName": "John",
        "fullName": "Rep. Garamendi, John [D-CA-8]",
        "lastName": "Garamendi",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "ADAPT Assets Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:51Z",
    "updateDateIncludingText": "2026-05-30T08:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
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
      "actionDate": "2026-05-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-04",
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
          "date": "2026-05-04T14:30:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8653ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8653\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Mr. Garamendi (for himself and Mr. Thompson of California ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to establish a grant program for demonstration projects that make critical transportation infrastructure resilient to natural hazards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accelerating Demonstration Approaches for Protecting Transportation Assets Act or the ADAPT Assets Act .\n#### 2. Accelerating Demonstration Approaches for Protecting Transportation Assets Program\n##### (a) In general\nThe Secretary of Transportation shall establish and carry out a competitive grant program, to be known as the Accelerating Demonstration Approaches for Protecting Transportation Assets Program (in this section referred to as the Program ), to provide up to 10 grants to eligible applicants for demonstration projects that make critical transportation infrastructure resilient to natural hazards.\n##### (b) Eligible applicants\nAn eligible applicant under the Program is\u2014\n**(1)**\na metropolitan planning organization (as defined in section 134 of title 23, United States Code);\n**(2)**\na State;\n**(3)**\na unit of local government;\n**(4)**\na public transportation agency or authority;\n**(5)**\na port or public toll authority that owns or operates eligible transportation assets;\n**(6)**\na Tribal government; or\n**(7)**\na consortium of 2 or more entities described in paragraphs (1) through (5), including a consortium led by a metropolitan planning organization, so long as the applicants demonstrate a regional partnership and governance structure for project delivery.\n##### (c) Application requirements\nTo be eligible for a grant under the Program, an eligible applicant shall submit to the Secretary an application at such time and containing such information as the Secretary may require.\n##### (d) Project selection criteria\nIn selecting projects under the Program, the Secretary shall consider, at a minimum, the extent to which the project\u2014\n**(1)**\naddresses existing or predicted recurring damage or asset failure of a high-risk transportation asset or corridor based on documented exposure to hazard risk;\n**(2)**\nprovides transportation system benefits, including preserving or enhancing regional or statewide mobility, economy, goods movement, safety, and emergency response access;\n**(3)**\nprovides additional benefits, including enhancing resilience of adjacent communities, the environment, and other critical infrastructure;\n**(4)**\nis consistent with a resilience improvement plan authorized under this Act;\n**(5)**\ndemonstrates readiness to proceed, including through\u2014\n**(A)**\ndemonstrating that it is supported by a regional partnership and governance plan that identifies roles, responsibilities, and decision-making processes across affected facility owners, land owners, funders, jurisdictions; and modes; and\n**(B)**\ncompletion of planning activities carried out in a manner consistent with section 168 of title 23, United States Code, or other key predevelopment milestones, or a credible schedule to complete such milestones; and\n**(6)**\nadvances innovation and replicability, including approaches that can be scaled by other regions.\n##### (e) Eligible uses\n**(1) In general**\nGrants under the Program may be used for a project or suite of projects within a region that, taken together, constitute a large-scale resilience investment to protect, elevate, adapt, relocate, or otherwise improve the resilience of transportation assets eligible for assistance under title 23, United States Code.\n**(2) Eligible uses**\nFunds provided by a grant under the Program may be used for\u2014\n**(A)**\npredevelopment activities, including data collection, engineering and design, environmental review, permitting, right-of-way activities, and procurement planning; and\n**(B)**\ncapital construction and implementation activities to harden or adapt transportation assets, including\u2014\n**(i)**\nprotective features described in section 119(k) of title 23, United States Code;\n**(ii)**\nsystem resilience improvements described in section 176(c)(3)(C) of title 23, United States Code;\n**(iii)**\nlevees, including engineered levees and levees utilizing natural infrastructure; and\n**(iv)**\nother resilience improvements that are functionally connected to making an eligible transportation asset more resilient to extreme weather, natural hazards, and disaster risks.\n##### (f) Multiyear project requirements\n**(1) Multiyear agreements**\nThe Secretary may enter into multiyear grant agreements to fund an eligible project under the Program across multiple fiscal years, including agreements that provide predictable funding for programmatic delivery of related resilience improvements.\n**(2) In general**\nTo be eligible for funding under a multiyear grant agreement described in paragraph (1), the project or suite of projects shall\u2014\n**(A)**\nhave an estimated total cost of not less than $500,000,000, except that the Secretary may reduce such threshold for Tribal applicants, rural regions, or insular areas; and\n**(B)**\ninvolve delivery challenges or institutional, regulatory, or funding barriers that are not routinely addressed through existing surface transportation programs and, if successfully resolved through the demonstration, would provide a replicable model for other projects.\n**(3) Eligible barriers**\nTo be considered eligible under paragraph (2)(B), the barriers described in such paragraph shall include 1 or more of the following:\n**(A)**\nMultiowner or multioperator governance and delivery structures.\n**(B)**\nIntegration of natural or nature-based infrastructure into transportation projects subject to Federal environmental review or permitting.\n**(C)**\nResilience investments located outside the transportation right-of-way that reduce risk to an eligible transportation asset.\n**(D)**\nProjects that protect or enhance transportation assets while also benefitting communities and other critical infrastructure systems.\n**(E)**\nProjects requiring coordinated funding across two or more Federal departments.\n##### (g) Federal share\n**(1) Federal share**\nThe Federal share of the cost of a project carried out with a grant under this section may not exceed 80 percent.\n**(2) Other Federal funds**\nOther Federal funds may be used to satisfy the non-Federal share only to the extent specifically provided for under the law authorizing the use of such Federal funds.\n##### (h) Administration\n**(1) Notice of funding opportunity**\nNot later than 180 days after the date of enactment of this Act, and annually thereafter, the Secretary shall publish a notice of funding opportunity for grants under the Program.\n**(2) Interagency coordination**\nIn carrying out the Program, the Secretary shall coordinate with other Federal departments and agencies, including the Environmental Protection Agency, Federal Emergency Management Agency, Department of Interior, Department of Commerce, and U.S. Army Corps of Engineers, to ensure Federal activities related to resiliency and Federal funding are streamlined and coordinated to allow for comprehensive solutions across Federal agencies to mitigate impacts from natural hazards on infrastructure, the economy, and the United States population.\n**(3) Relationship to other Federal programs**\nA grant under this section may be used in combination with funds made available under other provisions of law administered by the Department of Transportation, including funds for formula, discretionary, and emergency relief programs.\n**(4) Dashboard**\n**(A) In general**\nIn carrying out this section, the Secretary shall make publicly available in an easily identifiable location on the website of the Department of Transportation a dashboard containing the following information for each project in a grant agreement under this section:\n**(i)**\nProject name.\n**(ii)**\nProject sponsor.\n**(iii)**\nCity or urbanized area and State in which the project will be located.\n**(iv)**\nProject type.\n**(v)**\nAnticipated total project cost.\n**(vi)**\nAnticipated share of project costs to be sought under this section.\n**(vii)**\nDate of compliance with the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).\n**(viii)**\nDate on which the project entered the project development phase.\n**(ix)**\nDate on which the project entered the engineering phase, if applicable.\n**(x)**\nStatus of each permit necessary for the project to proceed, the Federal agency with principal responsibility for review of each necessary permit, and any participating agencies involved in the review of each necessary permit.\n**(xi)**\nStatus of the project sponsor in securing non-federal matching funds.\n**(xii)**\nDate on which a project grant agreement is anticipated to be executed.\n**(xiii)**\nFederal grant programs for which the project would also be eligible, if applicable.\n**(B) Updates**\nThe Secretary shall update the information provided under subparagraph (A) not less frequently than monthly.\n**(C) Project profiles**\nThe Secretary shall continue to make profiles for projects that are receiving assistance under this section publicly available in an easily identifiable location on the website of the Department of Transportation.\n##### (i) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary shall establish an interagency working group to develop and submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report not later than 4 years after the date of enactment of this Act, and every 2 years thereafter that\u2014\n**(1)**\ndescribes projects selected and funded under the Program;\n**(2)**\nevaluates the benefits of the projects\u2019 integration of natural and nature-based features in improving infrastructure resiliency;\n**(3)**\nevaluates program outcomes and best practices;\n**(4)**\nprovides recommendations regarding whether and how to scale the Program; and\n**(5)**\nprovides a benefit-cost analysis of each project selected and funded under the Program that uses the best available data, including\u2014\n**(A)**\nannual maintenance costs necessary for the upkeep of the project\u2019s components;\n**(B)**\nrisk to structures and infrastructure mitigated by the project;\n**(C)**\nlevel of protection provided by the project;\n**(D)**\nhistorical damage at the project location;\n**(E)**\ninformation on the benefitting area of the project; and\n**(F)**\nadditional data, as applicable.\n##### (j) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $2,000,000,000 for each of fiscal years 2027 through 2031, to remain available until expended, of which not more than 2 percent may be used for administrative expenses and technical assistance.\n##### (k) Definitions\nIn this section:\n**(1) Eligible transportation asset**\nThe term eligible transportation asset means\u2014\n**(A)**\na highway project eligible for assistance under title 23, United States Code;\n**(B)**\na public transportation facility or service eligible for assistance under chapter 53 of title 49, United States Code; or\n**(C)**\na port facility, including a facility that\u2014\n**(i)**\nconnects a port to other modes of transportation;\n**(ii)**\nimproves the efficiency of evacuations and disaster relief; or\n**(iii)**\naids transportation.\n**(2) Region**\nThe term region means\u2014\n**(A)**\nthe geographic area served by a metropolitan planning organization;\n**(B)**\na multijurisdictional area defined by a consortium of eligible applicants; or\n**(C)**\nsuch other area as the Secretary determines appropriate to address transportation system risk at a corridor or system scale.",
      "versionDate": "2026-05-04",
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
        "updateDate": "2026-05-21T18:42:31Z"
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
      "date": "2026-05-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8653ih.xml"
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
      "title": "ADAPT Assets Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T05:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ADAPT Assets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Accelerating Demonstration Approaches for Protecting Transportation Assets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to establish a grant program for demonstration projects that make critical transportation infrastructure resilient to natural hazards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T05:48:38Z"
    }
  ]
}
```
