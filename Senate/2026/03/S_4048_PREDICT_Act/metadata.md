# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4048?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4048
- Title: PREDICT Act
- Congress: 119
- Bill type: S
- Bill number: 4048
- Origin chamber: Senate
- Introduced date: 2026-03-11
- Update date: 2026-03-30T15:52:42Z
- Update date including text: 2026-03-30T15:52:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-11: Introduced in Senate
- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-11: Introduced in Senate

## Actions

- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-11",
    "latestAction": {
      "actionDate": "2026-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4048",
    "number": "4048",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "PREDICT Act",
    "type": "S",
    "updateDate": "2026-03-30T15:52:42Z",
    "updateDateIncludingText": "2026-03-30T15:52:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-03-11T14:29:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "NJ"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-11",
      "state": "ME"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "MS"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4048is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4048\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2026 Mr. Scott of South Carolina (for himself, Mr. Booker , Mr. Budd , Mr. King , Mr. Wicker , and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service to require the Secretary to award grants, contracts, or cooperative agreements to eligible entities to establish, maintain, or improve activities related to the detection and monitoring of infectious diseases through wastewater for public health emergency preparedness and response purposes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public health Response and Emergency Detection through Integrated wastewater Community Testing Act or the PREDICT Act .\n#### 2. Public health response and emergency detection through integrated wastewater surveillance\n##### (a) In general\nSubtitle C of title XXVIII of the Public Health Service Act ( 42 U.S.C. 300hh\u201331 et seq. ) is amended by adding at the end the following:\n2827. Wastewater surveillance for pathogen detection (a) Wastewater surveillance system The Secretary, acting through the Director of the Centers for Disease Control and Prevention (in this section referred to as the Secretary ), and in coordination with other Federal departments and agencies, shall award grants, contracts, or cooperative agreements to eligible entities to establish, maintain, or improve activities related to the detection and monitoring of infectious diseases through wastewater for public health emergency preparedness and response purposes. (b) Eligible entities To be eligible to receive an award under this section, an entity shall\u2014 (1) be a State, Tribal, or local health department, or a partnership between such a health department and other public and private entities; and (2) submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may reasonably require, which shall include\u2014 (A) a description of activities proposed to be carried out pursuant to an award under subsection (a); (B) factors such entity proposes to use to select wastewater sampling sites; (C) a plan for responding, as appropriate, to findings from such wastewater sampling, consistent with applicable plans developed by such entity pursuant to section 319C\u20131; (D) a plan to sustain such wastewater surveillance activities described in such application following the conclusion of the award period; and (E) any additional information the Secretary may require. (c) Consideration In making awards under subsection (a), the Secretary may give priority to eligible entities that have submitted an application that\u2014 (1) details plans to provide public access to data generated through such wastewater surveillance activities in a manner that enables comparison to such data generated by other recipients of an award under subsection (a); and (2) provides an assessment of community needs related to ongoing infectious disease monitoring, including burden of infectious diseases that can be detected in wastewater and availability of other forms of infectious disease surveillance. (d) Use of funds An eligible entity shall use amounts awarded under this section to\u2014 (1) establish, or enhance existing, capacity and capabilities to conduct wastewater sampling and related analysis; (2) conduct wastewater surveillance, as appropriate, at individual facilities, institutions, and locations in rural areas, in which there is an increased risk of infectious disease outbreaks and wastewater is not treated through the relevant local utility of the jurisdiction; and (3) implement projects that use evidence-based or promising practices to conduct wastewater surveillance activities. (e) Partnerships In carrying out activities under this section, eligible entities shall identify opportunities to partner with other public or private entities to leverage relevant capabilities maintained by such entities, as appropriate and consistent with this section. (f) Technical assistance The Secretary, in consultation with the heads of other applicable Federal agencies and departments, as appropriate, shall provide technical assistance to recipients of awards under this section to facilitate the planning, development, and implementation of activities described in subsection (d). (g) Wastewater surveillance guidance Not later than 180 days after the date of enactment of the PREDICT Act , the Secretary shall issue draft guidance\u2014 (1) to provide recommendations for recipients of awards under this section regarding\u2014 (A) the use of assays to promote efficient wastewater surveillance; and (B) the use of assays for data on multiple infectious diseases; and (2) to establish standards for\u2014 (A) wastewater testing methods and metrics used by such recipients that\u2014 (i) use a consistent protocol and process; and (ii) sample using scientifically rigorous and sensitive methods; and (B) wastewater sample data reporting by such recipients to the Secretary, to be published by the Secretary in a publicly available wastewater surveillance database and dashboard. (h) Authorization of appropriations To carry out this section, there is authorized to be appropriated such sums as may be necessary for each of fiscal years 2026 through 2030. .\n##### (b) Wastewater surveillance research\n**(1) In general**\nThe Secretary of Health and Human Services (in this subsection referred to as the Secretary ) shall continue to conduct or support research on the use of wastewater surveillance to detect and monitor emerging infectious diseases, which may include\u2014\n**(A)**\nresearch to improve the efficiency of wastewater sample collection and analysis and increase the sensitivity and specificity of wastewater testing methods; and\n**(B)**\nimplementation and development of evidence-based practices to facilitate the estimation of population-level data within a community.\n**(2) Non-duplication of effort**\nThe Secretary shall ensure that activities carried out under this subsection do not unnecessarily duplicate efforts of other agencies and offices within the Department of Health and Human Services related to wastewater surveillance.",
      "versionDate": "2026-03-11",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-03-30T15:52:42Z"
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
      "date": "2026-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4048is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "PREDICT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PREDICT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Public health Response and Emergency Detection through Integrated wastewater Community Testing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service to require the Secretary to award grants, contracts, or cooperative agreements to eligible entities to establish, maintain, or improve activities related to the detection and monitoring of infectious diseases through wastewater for public health emergency preparedness and response purposes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T04:03:30Z"
    }
  ]
}
```
