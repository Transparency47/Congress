# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1217?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1217
- Title: Orphan Well Grant Flexibility Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1217
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2026-03-30T14:11:32Z
- Update date including text: 2026-03-30T14:11:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1217",
    "number": "1217",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Orphan Well Grant Flexibility Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-30T14:11:32Z",
    "updateDateIncludingText": "2026-03-30T14:11:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "KS"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1217ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1217\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Thompson of Pennsylvania (for himself and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Energy Policy Act of 2005 to address measuring methane emissions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Orphan Well Grant Flexibility Act of 2025 .\n#### 2. Pre-plugging methane emissions for grant eligibility\nSection 349 of the Energy Policy Act of 2005 ( 42 U.S.C. 15907 ) is amended\u2014\n**(1)**\nin subsection (c)(2), by adding at the end the following:\n(C) Activities not required Nothing in this section requires a State to measure methane emissions or conduct other activities described in subparagraph (A), which are activities a State may conduct but is not required to conduct, as a condition of eligibility for a grant under this subsection. ; and\n**(2)**\nin subsection (f)(2), in the matter preceding subparagraph (A), by inserting , which may include estimates derived from pre-plugging or post-plugging monitoring data that States may, but are not required to, collect using funding from grants awarded under this section, after estimate .\n#### 3. National Academies study on community impact of orphaned well grant program\n##### (a) Study\nNot later than 180 days after the date of enactment of this Act, the Secretary of the Interior shall\u2014\n**(1)**\nseek to enter into an agreement with the National Academies of Sciences, Engineering, and Medicine under which the National Academies of Sciences, Engineering, and Medicine shall carry out a study on the effect of the plugging and remediation activity conducted under section 349 of the Energy Policy Act of 2005 ( 42 U.S.C. 15907 ) on economic development, housing trends, and other potential benefits (such as improvements in water quality) in areas where the plugging and remediation activity conducted under that section reclaimed a high number of sites, as determined by the National Academies of Sciences, Engineering, and Medicine; and\n**(2)**\nto the maximum extent practicable, provide the National Academies of Sciences, Engineering, and Medicine with information necessary to carry out the study described in paragraph (1).\n##### (b) Key inputs\nThe National Academies of Sciences, Engineering, and Medicine shall ensure that at least 1 State from each region of the United States (Northeast, Southwest, West, Southeast, and Midwest) shall be key inputs to the study carried out under subsection (a).\n##### (c) Consultation\nIn carrying out the study under subsection (a), the National Academies of Sciences, Engineering, and Medicine shall consult with\u2014\n**(1)**\nthe Department of Housing and Urban Development, with respect to\u2014\n**(A)**\nhow the plugging and remediation activity conducted under section 349 of the Energy Policy Act of 2005 ( 42 U.S.C. 15907 ) has affected economic development and housing trends; and\n**(B)**\nhow data on locations of plugging and remediation priorities from the Department of the Interior may be valuable to the Department of Housing and Urban Development;\n**(2)**\nthe Interstate Oil and Gas Compact Commission, to provide data required to carry out the study under subsection (a); and\n**(3)**\nother Federal agencies, as determined by the Secretary of the Interior, in consultation with the National Academies of Sciences, Engineering, and Medicine.\n##### (d) Report\nNot later than 18 months after the date on which the last grant is awarded under section 349 of the Energy Policy Act of 2005 ( 42 U.S.C. 15907 ), the National Academies of Sciences, Engineering, and Medicine shall submit to Congress a report detailing the findings of the study carried out under subsection (a).\n##### (e) Use of existing funds\nThis section shall be carried out using amounts otherwise made available to the Secretary of the Interior.",
      "versionDate": "2025-02-11",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-28T19:34:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1217",
          "measure-number": "1217",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1217v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Orphan Well Grant Flexibility Act of 2025</strong></p><p>This bill removes certain requirements, including measuring methane emissions, for grants to states under the\u00a0State Orphaned Wells Program.</p><p>Under the program, the Department of the Interior provides grants to states for the following purposes: (1) plugging,\u00a0remediating, and reclaiming orphaned wells located on federal land; (2) identifying and characterizing undocumented orphaned wells; (3) measuring and tracking emissions of gases (e.g., methane) or contamination of water associated with orphaned wells; or (4) conducting certain other related activities.\u00a0Generally, <em>orphaned wells</em> are oil and gas wells without solvent owners or operators responsible for cleaning up leaks from the wells.\u00a0</p><p>In 2024, Interior issued guidance for the grant program that requires states to conduct certain measuring and tracking activities related to the orphaned wells before and after receiving grants. However, the bill specifies that states are not required to provide such information in order to receive a grant. Instead, the bill makes measuring and tracking optional.</p><p>The bill also directs Interior to enter into an agreement with the National Academies of Sciences, Engineering, and Medicine to study the effect of the plugging and remediation activity on economic development, housing trends, and other potential benefits in areas where the plugging and remediation activity reclaimed a high number of well sites.</p>"
        },
        "title": "Orphan Well Grant Flexibility Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1217.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Orphan Well Grant Flexibility Act of 2025</strong></p><p>This bill removes certain requirements, including measuring methane emissions, for grants to states under the\u00a0State Orphaned Wells Program.</p><p>Under the program, the Department of the Interior provides grants to states for the following purposes: (1) plugging,\u00a0remediating, and reclaiming orphaned wells located on federal land; (2) identifying and characterizing undocumented orphaned wells; (3) measuring and tracking emissions of gases (e.g., methane) or contamination of water associated with orphaned wells; or (4) conducting certain other related activities.\u00a0Generally, <em>orphaned wells</em> are oil and gas wells without solvent owners or operators responsible for cleaning up leaks from the wells.\u00a0</p><p>In 2024, Interior issued guidance for the grant program that requires states to conduct certain measuring and tracking activities related to the orphaned wells before and after receiving grants. However, the bill specifies that states are not required to provide such information in order to receive a grant. Instead, the bill makes measuring and tracking optional.</p><p>The bill also directs Interior to enter into an agreement with the National Academies of Sciences, Engineering, and Medicine to study the effect of the plugging and remediation activity on economic development, housing trends, and other potential benefits in areas where the plugging and remediation activity reclaimed a high number of well sites.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr1217"
    },
    "title": "Orphan Well Grant Flexibility Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Orphan Well Grant Flexibility Act of 2025</strong></p><p>This bill removes certain requirements, including measuring methane emissions, for grants to states under the\u00a0State Orphaned Wells Program.</p><p>Under the program, the Department of the Interior provides grants to states for the following purposes: (1) plugging,\u00a0remediating, and reclaiming orphaned wells located on federal land; (2) identifying and characterizing undocumented orphaned wells; (3) measuring and tracking emissions of gases (e.g., methane) or contamination of water associated with orphaned wells; or (4) conducting certain other related activities.\u00a0Generally, <em>orphaned wells</em> are oil and gas wells without solvent owners or operators responsible for cleaning up leaks from the wells.\u00a0</p><p>In 2024, Interior issued guidance for the grant program that requires states to conduct certain measuring and tracking activities related to the orphaned wells before and after receiving grants. However, the bill specifies that states are not required to provide such information in order to receive a grant. Instead, the bill makes measuring and tracking optional.</p><p>The bill also directs Interior to enter into an agreement with the National Academies of Sciences, Engineering, and Medicine to study the effect of the plugging and remediation activity on economic development, housing trends, and other potential benefits in areas where the plugging and remediation activity reclaimed a high number of well sites.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr1217"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1217ih.xml"
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
      "title": "Orphan Well Grant Flexibility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T12:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Orphan Well Grant Flexibility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T12:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Energy Policy Act of 2005 to address measuring methane emissions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T12:48:43Z"
    }
  ]
}
```
