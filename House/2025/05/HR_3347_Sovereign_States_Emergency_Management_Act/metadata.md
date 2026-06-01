# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3347?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3347
- Title: Sovereign States Emergency Management Act
- Congress: 119
- Bill type: HR
- Bill number: 3347
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2026-05-16T08:07:35Z
- Update date including text: 2026-05-16T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- 2025-05-14 - Committee: Referred to the Subcommittee on Emergency Management and Technology.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- 2025-05-14 - Committee: Referred to the Subcommittee on Emergency Management and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3347",
    "number": "3347",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Sovereign States Emergency Management Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:35Z",
    "updateDateIncludingText": "2026-05-16T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Emergency Management and Technology.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-13",
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
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-14T20:30:16Z",
              "name": "Referred to"
            }
          },
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-13T16:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-13T21:15:58Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3347ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3347\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Higgins of Louisiana introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo abolish FEMA and establish a block grant program for disaster relief, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sovereign States Emergency Management Act .\n#### 2. Abolishment of FEMA\n##### (a) Abolishment\nThe Federal Emergency Management Agency is abolished effective on the date that is 2 years after the date of enactment of this Act.\n##### (b) Unobligated funds\nAny funds made available to the Administrator of the Federal Emergency Management Agency that are unobligated on the abolishment date described in subsection (a) shall be transferred to the general fund of the Treasury and made available to carry out the program established under section 2.\n##### (c) Transfer of functions\nAll functions that immediately before the abolishment date specified in subsection (a) are authorized to be performed by the Administrator of the Federal Emergency Management Agency, any other officer or employee of the Agency acting in that capacity, or any agency or office of the Agency, are transferred to the President effective on such abolishment date.\n##### (d) Personnel and assets\nExcept as otherwise provided in this Act, so much of the personnel, property, and records employed, used, held, available, or to be made available in connection with a function transferred to the President under subsection (c) shall be available to the President, at such time or times as the President directs for use in connection with the functions transferred.\n##### (e) References\nAny reference in any other Federal law, Executive order, rule, regulation, or delegation of authority, or any document of or pertaining to the Federal Emergency Management Agency\u2014\n**(1)**\nto the Administrator of the Federal Emergency Management Agency is deemed to refer to the President; or\n**(2)**\nto the Federal Emergency Management Agency is deemed to refer to the Executive Office of the President.\n#### 3. Disaster relief block grant program\n##### (a) Establishment\nThe Secretary of the Treasury shall establish a program to provide grants to States for natural disaster and emergency relief.\n##### (b) Grant terms\n**(1) In general**\nIn carrying out the program established under this section, the Secretary shall provide a grant to each State in an amount determined in accordance with the formula established pursuant to paragraph (2).\n**(2) Allocation of funds**\n**(A) In general**\nThe Secretary shall, by rule, establish a formula for the allocation of grant funds to each State under this section.\n**(B) Considerations**\nIn establishing the formula under subparagraph (A), the Secretary shall consider the following:\n**(i)**\nPopulation size.\n**(ii)**\nHistorical disaster frequency and severity during the 20-year period preceding the date of enactment of this Act.\n**(iii)**\nGeographic risk factors (such as seismic zones, flood plains, hurricane-prone areas).\n**(iv)**\nEconomic need, as determined by per capita income.\n**(3) Use of funds**\nA State may use a grant provided under this section to carry out\u2014\n**(A)**\ndisaster preparedness training and acquire and maintain related equipment;\n**(B)**\nresponse and recovery operations following a natural disaster or emergency; and\n**(C)**\nmitigation projects to reduce future disaster risks.\n**(4) Administrative costs**\nA State may use not more than 5 percent of the amount allocated to such State under this subsection for administrative costs.\n**(5) Allocation**\nThe Secretary may not allocate grant funds to a State for a fiscal year under this section unless and until the Secretary, pursuant to subsection (c), approves the emergency management plan submitted by such State for such fiscal year.\n##### (c) State emergency management plans\nNot later than April 1 of each year, each State shall develop and submit for approval by the Secretary an emergency management plan for the fiscal year beginning on October 1 of such year, and such plan shall include\u2014\n**(1)**\na description of how the State intends to use funds allocated under this section;\n**(2)**\ndocumentation of coordination between the State, local governments, and Tribal authorities in developing and implementing such emergency management plan; and\n**(3)**\nmeasurable goals for disaster preparedness and response.\n##### (d) Reports\nNot later than 90 days after the end of each fiscal year, each State shall submit to the Secretary a report describing\u2014\n**(1)**\nhow funds allocated under this section were used during the preceding fiscal year;\n**(2)**\noutcomes achieved with such funds, including improvements in preparedness metrics, response times, and completed mitigation projects; and\n**(3)**\nthe extent to which the State complied with the emergency management plan developed under subsection (c).\n##### (e) Duplication of benefits\nThe Secretary shall ensure that no State receives a grant under this section if such State receives assistance from any other Federal source for the same purposes for which such a grant may be used.\n##### (f) Audit\nNot less frequently than annually, the Secretary shall conduct an audit of the program established under this section and submit a report thereon to the Committees on Oversight and Government Reform, Homeland Security, and Transportation and Infrastructure of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate.\n##### (g) Administrative and audit expenses\nOf the amounts made available to carry out this section, 10 percent shall be for expenses related to administering the program established under this section and 10 percent shall be for expenses related to carrying out the audit of such program required under subsection (f).\n##### (h) Termination\nThe program established under this section shall terminate on the date that is 4 years after the date on which the Secretary issues the rule required by subsection (b)(2).\n##### (i) Definitions\nIn this section:\n**(1) Emergency**\nThe term emergency means an occasion or instance for which assistance is needed to save lives and to protect property and public health and safety, or to lessen or avert the threat of a catastrophe in any part of a State.\n**(2) Natural disaster**\nThe term natural disaster means any natural catastrophe (including any hurricane, tornado, storm, high water, winddriven water, tidal wave, tsunami, earthquake, volcanic eruption, landslide, mudslide, snowstorm, or drought), or, regardless of cause, any fire, flood, or explosion, in any part of a State, for which assistance is needed to alleviate the damage, loss, hardship, or suffering caused thereby.\n**(3) State**\nThe term State any of the fifty States, the District of Columbia, Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.",
      "versionDate": "2025-05-13",
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
        "updateDate": "2025-06-09T14:55:16Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3347ih.xml"
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
      "title": "Sovereign States Emergency Management Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sovereign States Emergency Management Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To abolish FEMA and establish a block grant program for disaster relief, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:48:35Z"
    }
  ]
}
```
