# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4560?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4560
- Title: Building Resilient Infrastructure and Communities for All Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4560
- Origin chamber: House
- Introduced date: 2025-07-21
- Update date: 2025-09-11T08:06:11Z
- Update date including text: 2025-09-11T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-22 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-07-21: Introduced in House

## Actions

- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-22 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4560",
    "number": "4560",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "F000481",
        "district": "2",
        "firstName": "Shomari",
        "fullName": "Rep. Figures, Shomari [D-AL-2]",
        "lastName": "Figures",
        "party": "D",
        "state": "AL"
      }
    ],
    "title": "Building Resilient Infrastructure and Communities for All Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-11T08:06:11Z",
    "updateDateIncludingText": "2025-09-11T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T16:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-22T17:05:32Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
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
      "sponsorshipDate": "2025-08-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4560ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4560\nIN THE HOUSE OF REPRESENTATIVES\nJuly 21, 2025 Mr. Figures (for himself and Mr. Edwards ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide requirements relating to the funding of predisaster hazard mitigation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Building Resilient Infrastructure and Communities for All Act of 2025 .\n#### 2. Predisaster hazard mitigation\n##### (a) In general\nSection 203 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133 ) is amended\u2014\n**(1)**\nin subsection (c) by striking or local government in each place it appears;\n**(2)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A) by striking not fewer than five local governments to receive assistance under this section and inserting projects to receive assistance under this section that are cost-effective and designed to reduce injuries, loss of life, and damage and destruction of property, including damage to critical services and facilities ; and\n**(ii)**\nby striking subparagraph (C);\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A) by striking in providing assistance to local governments under this section, the President shall select from local governments recommended by the Governors under this subsection. and inserting a State that receives funds under this section may use such funds only for projects recommended under paragraph (1)(A) ; and\n**(ii)**\nby striking subparagraph (B) and inserting the following:\n(B) Presidential approval The President may approve a project that has not been recommended by a Governor under this subsection as an eligible use of funds if the President determines that extraordinary circumstances justify the selection and that making the selection will further the purpose of this section. ; and\n**(C)**\nin paragraph (3) by striking the President may select, subject to the criteria specified in subsection (g), any local governments of the State to receive assistance under this section. and inserting such State may not receive funds under the formula described in subsection (f)(2). ;\n**(3)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking on a competitive basis and inserting to a State or an Indian tribal government through a direct allocation based on the formula described in paragraph (2) ; and\n**(ii)**\nby striking and in accordance with the criteria in subsection (g) ;\n**(B)**\nby striking paragraph (2) and inserting the following:\n(2) Formula In providing financial assistance under this section, the President shall distribute to each eligible State available funds for a fiscal year using the following formula: (A) Thirty-three percent of available funds shall be distributed equally among each eligible State. (B) Thirty-three percent of available funds shall be distributed among each eligible State in a proportion that gives preference to such States that have a higher population, using data from the most recent census of the United States. (C) Thirty-three percent of available funds shall be distributed among each eligible State in a proportion that gives preference to States that have the most vulnerability to natural hazards in the critical infrastructure of such States. ;\n**(C)**\nin paragraph (3)(B) by striking on a competitive basis pursuant to paragraph (1) and inserting under this section ; and\n**(D)**\nby adding at the end the following:\n(4) Tribes In providing financial assistance under this section, the President shall ensure that the amount of financial assistance made available to an Indian tribal government is not less than $75,000,000. (5) Suballocation Each State that receives assistance under this section shall distribute\u2014 (A) not less than 50 percent of the funds distributed under this subsection to the local government carrying out a project recommended under subsection (d)(1); and (B) any funds not distributed under (A) to activities described in subsections (b) and (e) of section 203. (6) Additional eligibility for hazard mitigation assistance The receipt of funds for a project under this section may not be considered in determining eligibility for funding under section 404 for such project. ;\n**(4)**\nin subsection (g)\u2014\n**(A)**\nby striking In determining whether to provide technical and financial assistance to a State or local government under this section, the President shall provide financial assistance only in States that have and inserting The President may only provide financial assistance under this section to a State that has ; and\n**(B)**\nby striking of such States and all that follows through in consultation with State and local governments. and inserting of such States. ; and\n**(5)**\nin subsection (h) by striking mitigation activities approved by the President and inserting mitigation activities under this section .\n##### (b) Hazard mitigation\nSection 404 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170c ) is amended by adding at the end the following:\n(h) Additional eligibility for predisaster hazard mitigation assistance The receipt of funds for a project under this section may not be considered in determining eligibility for funding under section 203 for such project. .",
      "versionDate": "2025-07-21",
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
        "name": "Emergency Management",
        "updateDate": "2025-07-31T22:27:29Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4560ih.xml"
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
      "title": "Building Resilient Infrastructure and Communities for All Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Building Resilient Infrastructure and Communities for All Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide requirements relating to the funding of predisaster hazard mitigation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T05:18:38Z"
    }
  ]
}
```
