# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1545?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1545
- Title: Repeatedly Flooded Communities Preparation Act
- Congress: 119
- Bill type: S
- Bill number: 1545
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2025-05-29T12:24:50Z
- Update date including text: 2025-05-29T12:24:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-05-01 - Committee: Committee on Banking, Housing, and Urban Affairs. Hearings held.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-05-01 - Committee: Committee on Banking, Housing, and Urban Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1545",
    "number": "1545",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
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
    "title": "Repeatedly Flooded Communities Preparation Act",
    "type": "S",
    "updateDate": "2025-05-29T12:24:50Z",
    "updateDateIncludingText": "2025-05-29T12:24:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Banking, Housing, and Urban Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
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
        "item": [
          {
            "date": "2025-05-01T17:32:03Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-04-30T23:28:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1545is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1545\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Scott of South Carolina (for himself and Mr. Schatz ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the National Flood Insurance Act of 1968 to ensure community accountability for areas repeatedly damaged by floods, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Repeatedly Flooded Communities Preparation Act .\n#### 2. Community accountability for repeatedly flooded areas\n##### (a) In general\nSection 1361 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4102 ) is amended by adding at the end the following:\n(e) Community accountability for repeatedly damaged areas (1) Definitions In this subsection\u2014 (A) the term covered community means a community\u2014 (i) that is participating in the national flood insurance program under section 1315; and (ii) within which are located\u2014 (I) not fewer than 50 repetitive loss structures with respect to each of which, during any 10-year period, there have been not fewer than 2 claims for payments under flood insurance coverage for a total amount that is more than $1,000; (II) not fewer than 5 severe repetitive loss structures for which mitigation activities meeting the standards for approval under section 1366(c)(2)(A) have not been conducted; or (III) a public facility or a private nonprofit facility that has received assistance for repair, restoration, reconstruction, or replacement under section 406 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5172 ) relating to more than 1 flooding event during the most recent 10-year period; (B) the terms private nonprofit facility and public facility have the meanings given those terms in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ); and (C) the term severe repetitive loss structure has the meaning given the term in section 1366(h). (2) Requirements for covered communities The Administrator shall, by regulation, require a covered community to\u2014 (A) determine the areas within the covered community in which properties described in paragraph (1)(A)(ii) or flood-damaged facilities are located in order to identify areas that are repeatedly damaged by floods; (B) assess, with assistance from the Administrator, the continuing risks to the repeatedly damaged areas identified under subparagraph (A); (C) develop a community-specific plan for mitigating continuing flood risks to the repeatedly damaged areas identified under subparagraph (A); (D) submit the plan described in subparagraph (C), and any plan updates, to the Administrator at appropriate intervals; (E) implement the plan described in subparagraph (C) and any updates to the plan; and (F) subject to section 552a of title 5, United States Code, make the plan described in subparagraph (C), any updates to the plan, and reports on progress in reducing flood risk available to the public. (3) Incorporation into existing plans A covered community may incorporate a plan developed under paragraph (2)(C), including any updates to such a plan, into a mitigation plan developed under\u2014 (A) section 1366; and (B) section 322 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5165 ). (4) Assistance to communities (A) Data To assist a covered community in developing a plan required under paragraph (2)(C), including any updates to such a plan, the Administrator shall, upon request, provide the covered community with appropriate data regarding the property addresses and dates of claims associated with insured properties within the covered community. (B) Mitigation grants In making a determination regarding financial assistance under this Act, the Administrator may consider the extent to which a covered community\u2014 (i) has complied with this subsection; and (ii) is working to remedy problems with respect to repeatedly flooded areas. (5) Sanctions (A) In general The Administrator may, by regulations issued in accordance with the procedures required under section 553 of title 5, United States Code, impose appropriate sanctions on a covered community that fails to\u2014 (i) comply with this subsection; or (ii) make sufficient progress in reducing the flood risks to areas in the covered community that are repeatedly damaged by floods. (B) Suspension and probation The sanctions described in subparagraph (A) may include suspension from the national flood insurance program or probation under that program, as provided under section 59.24 of title 44, Code of Federal Regulations, as in effect on the date of enactment of this subsection. (C) Notice (i) In general Before imposing any sanctions under this paragraph, the Administrator shall provide the covered community that is subject to the sanctions with notice of the violation that may subject the covered community to the sanctions. (ii) Contents The notice required under clause (i) shall include recommendations for actions that the covered community receiving the notice may take in order to bring the covered community into compliance. (D) Considerations In determining appropriate sanctions to impose under this paragraph, the Administrator shall consider the resources available to the covered community that is subject to the sanctions, including\u2014 (i) any Federal funding received by the covered community; (ii) the portion of the covered community that lies within an area having special flood hazards; and (iii) any other factor that makes it difficult for the covered community to conduct mitigation activities for flood-prone structures. (6) Reports to Congress Not later than 6 years after the date of enactment of this subsection, and not less frequently than once every 2 years thereafter, the Administrator shall submit to Congress a report regarding the progress made by covered communities with respect to implementing plans developed under paragraph (2)(C), including any updates to those plans. .\n##### (b) Regulations\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency shall issue regulations necessary to carry out subsection (e) of section 1361 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4102 ), as added by subsection (a) of this section.",
      "versionDate": "2025-04-30",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-05-29T15:28:24Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-29T15:28:24Z"
          },
          {
            "name": "Department of Homeland Security",
            "updateDate": "2025-05-29T15:28:24Z"
          },
          {
            "name": "Disaster relief and insurance",
            "updateDate": "2025-05-29T15:28:24Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2025-05-29T15:28:24Z"
          },
          {
            "name": "Federal Emergency Management Agency (FEMA)",
            "updateDate": "2025-05-29T15:28:24Z"
          },
          {
            "name": "Floods and storm protection",
            "updateDate": "2025-05-29T15:28:24Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-29T15:28:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-29T12:24:50Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1545is.xml"
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
      "title": "Repeatedly Flooded Communities Preparation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Repeatedly Flooded Communities Preparation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Flood Insurance Act of 1968 to ensure community accountability for areas repeatedly damaged by floods, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:48:30Z"
    }
  ]
}
```
