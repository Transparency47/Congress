# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3291?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3291
- Title: Certainty for Our Energy Future Act
- Congress: 119
- Bill type: HR
- Bill number: 3291
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-05-18T18:34:21Z
- Update date including text: 2026-05-18T18:34:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3291",
    "number": "3291",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Certainty for Our Energy Future Act",
    "type": "HR",
    "updateDate": "2026-05-18T18:34:21Z",
    "updateDateIncludingText": "2026-05-18T18:34:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NY"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "WA"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NV"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-05-09",
      "state": "GA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "AZ"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-06-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3291ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3291\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mrs. Kiggans of Virginia (for herself, Mr. Garbarino , Mr. Valadao , Mr. Newhouse , and Mr. Amodei of Nevada ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to terminate the clean electricity production credit and clean electricity investment credit with respect to certain technologies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Certainty for Our Energy Future Act .\n#### 2. Termination of clean electricity production credit with respect to certain technologies\n##### (a) In general\nSection 45Y(d) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraphs:\n(4) Special rule for wind and solar energy The term qualified facility shall not include any facility used for the generation of electricity using wind or solar energy the construction of which begins after December 31, 2030. (5) Beginning of construction definition For purposes of determining when construction begins for purposes of this section, principles similar to those under Notice 2013\u201329, 2013\u201320 I.R.B. 1085, and any subsequent guidance clarifying, modifying, or updating such notice, as in effect on January 1, 2025, including the Physical Work Test, Five Percent Safe Harbor, Continuity Requirement, and Continuity Safe Harbor, shall apply. .\n##### (b) Effective date\nThe amendment made by this section shall take effect on January 1, 2026.\n#### 3. Termination of clean electricity investment credit with respect to certain technologies\n##### (a) In general\nSection 48E(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraphs:\n(4) Special rule for wind and solar energy The term qualified facility shall not include any facility used for the generation of electricity using wind or solar energy the construction of which begins after December 31, 2030. (5) Beginning of construction definition For purposes of determining when construction begins for purposes of this section, principles similar to those under Notice 2013\u201329, 2013\u201320 I.R.B. 1085, and any subsequent guidance clarifying, modifying, or updating such notice, as in effect on January 1, 2025, including the Physical Work Test, Five Percent Safe Harbor, Continuity Requirement, and Continuity Safe Harbor, shall apply. .\n##### (b) Effective date\nThe amendment made by this section shall take effect on January 1, 2026.\n#### 4. Denial of clean energy tax benefits to companies connected to countries of concern\n##### (a) In general\nChapter 77 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n7531. Denial of clean energy tax benefits to companies connected to countries of concern (a) In general In the case of any taxpayer that is a disqualified company, this title shall be applied without regard to sections 30C, 40, 40A, 40B, 45, 45Q, 45U, 45V, 45W, 45X, 45Y, 45Z, 48, 48C, 48E, 179D, 6426(c), 6426(d), 6426(e), and 6427(e). (b) Disqualified company For purposes of this section\u2014 (1) In general The term disqualified company means any entity\u2014 (A) created or organized under the laws of, or controlled by, one or more governments of a foreign country that is a country of concern, or (B) controlled (in the aggregate) by one or more entities described in subparagraph (A). (2) Country of concern The term country of concern means the People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, or the Democratic People\u2019s Republic of Korea. (3) Control The term control has the meaning given such term under section 954(d)(3), determined by treating the rules of section 958(a)(2) as applying to both foreign and domestic corporations, partnerships, trusts, and estates. (4) Government of a foreign country The term government of a foreign country means a national government of a foreign country, an agency or government instrumentality of a national government of a foreign country, a dominant or ruling political party of a foreign country, or any individual currently in a senior role of a country of concern and with substantial authority over policy, operations, or the use of government-owned resources of the foreign country. .\n##### (b) Clerical amendment\nThe table of sections for chapter 77 of such Code is amended by adding at the end the following new item:\nSec. 7531. Denial of clean energy tax benefits to companies connected to countries of concern. .\n##### (c) Guidance\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary\u2019s delegate) shall issue guidance regarding implementation of this section.\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning on or after the date that is 180 days after the date on which the Secretary publishes guidance under subsection (c).",
      "versionDate": "2025-05-08",
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
        "name": "Taxation",
        "updateDate": "2025-06-06T18:15:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-08",
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
          "measure-id": "id119hr3291",
          "measure-number": "3291",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-08",
          "originChamber": "HOUSE",
          "update-date": "2026-05-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3291v00",
            "update-date": "2026-05-18"
          },
          "action-date": "2025-05-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Certainty for Our Energy Future\u00a0Act</strong></p><p>This bill\u00a0terminates federal tax credits for certain investments in and the production of electricity using wind and solar energy. The bill also prohibits certain entities connected with China, Russia, Iran, or North Korea from claiming various energy-related federal tax incentives.</p><p>The bill terminates the federal clean electricity investment tax credit and the federal clean electricity production tax credit for investments in and electricity produced by a facility (1) used to generate electricity using wind or solar energy,\u00a0and (2) for which construction begins after 2030.\u00a0</p><p>The bill also prohibits an entity that is created or organized under the laws of or controlled by\u00a0the government of\u00a0China, Russia, Iran, or North Korea, or an entity controlled by one or more of such entities, from claiming the federal tax credits for</p><ul><li>alternative fuel vehicle refueling property,</li><li>second-generation\u00a0biofuel,</li><li>biodiesel fuel,</li><li>sustainable aviation fuel,</li><li>renewable electricity production,</li><li>carbon sequestration,</li><li>zero-emission nuclear power production,</li><li>clean hydrogen production,</li><li>clean commercial vehicles,</li><li>advanced manufacturing production,</li><li>clean electricity production,</li><li>clean fuel production,</li><li>investments in energy property,</li><li>advanced energy projects,</li><li>clean electricity investment,</li><li>biodiesel mixtures,</li><li>alternative fuel, or</li><li>alternative fuel mixtures.</li></ul><p>Further, such entities are prohibited from claiming the federal tax deduction for energy efficient improvements to commercial buildings.</p><p>Finally, such entities are not entitled to a credit or refund of federal excise taxes paid\u00a0on biodiesel, alternative fuel, or sustainable aviation fuel mixtures produced by the entities.</p>"
        },
        "title": "Certainty for Our Energy Future Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3291.xml",
    "summary": {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Certainty for Our Energy Future\u00a0Act</strong></p><p>This bill\u00a0terminates federal tax credits for certain investments in and the production of electricity using wind and solar energy. The bill also prohibits certain entities connected with China, Russia, Iran, or North Korea from claiming various energy-related federal tax incentives.</p><p>The bill terminates the federal clean electricity investment tax credit and the federal clean electricity production tax credit for investments in and electricity produced by a facility (1) used to generate electricity using wind or solar energy,\u00a0and (2) for which construction begins after 2030.\u00a0</p><p>The bill also prohibits an entity that is created or organized under the laws of or controlled by\u00a0the government of\u00a0China, Russia, Iran, or North Korea, or an entity controlled by one or more of such entities, from claiming the federal tax credits for</p><ul><li>alternative fuel vehicle refueling property,</li><li>second-generation\u00a0biofuel,</li><li>biodiesel fuel,</li><li>sustainable aviation fuel,</li><li>renewable electricity production,</li><li>carbon sequestration,</li><li>zero-emission nuclear power production,</li><li>clean hydrogen production,</li><li>clean commercial vehicles,</li><li>advanced manufacturing production,</li><li>clean electricity production,</li><li>clean fuel production,</li><li>investments in energy property,</li><li>advanced energy projects,</li><li>clean electricity investment,</li><li>biodiesel mixtures,</li><li>alternative fuel, or</li><li>alternative fuel mixtures.</li></ul><p>Further, such entities are prohibited from claiming the federal tax deduction for energy efficient improvements to commercial buildings.</p><p>Finally, such entities are not entitled to a credit or refund of federal excise taxes paid\u00a0on biodiesel, alternative fuel, or sustainable aviation fuel mixtures produced by the entities.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119hr3291"
    },
    "title": "Certainty for Our Energy Future Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Certainty for Our Energy Future\u00a0Act</strong></p><p>This bill\u00a0terminates federal tax credits for certain investments in and the production of electricity using wind and solar energy. The bill also prohibits certain entities connected with China, Russia, Iran, or North Korea from claiming various energy-related federal tax incentives.</p><p>The bill terminates the federal clean electricity investment tax credit and the federal clean electricity production tax credit for investments in and electricity produced by a facility (1) used to generate electricity using wind or solar energy,\u00a0and (2) for which construction begins after 2030.\u00a0</p><p>The bill also prohibits an entity that is created or organized under the laws of or controlled by\u00a0the government of\u00a0China, Russia, Iran, or North Korea, or an entity controlled by one or more of such entities, from claiming the federal tax credits for</p><ul><li>alternative fuel vehicle refueling property,</li><li>second-generation\u00a0biofuel,</li><li>biodiesel fuel,</li><li>sustainable aviation fuel,</li><li>renewable electricity production,</li><li>carbon sequestration,</li><li>zero-emission nuclear power production,</li><li>clean hydrogen production,</li><li>clean commercial vehicles,</li><li>advanced manufacturing production,</li><li>clean electricity production,</li><li>clean fuel production,</li><li>investments in energy property,</li><li>advanced energy projects,</li><li>clean electricity investment,</li><li>biodiesel mixtures,</li><li>alternative fuel, or</li><li>alternative fuel mixtures.</li></ul><p>Further, such entities are prohibited from claiming the federal tax deduction for energy efficient improvements to commercial buildings.</p><p>Finally, such entities are not entitled to a credit or refund of federal excise taxes paid\u00a0on biodiesel, alternative fuel, or sustainable aviation fuel mixtures produced by the entities.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119hr3291"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3291ih.xml"
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
      "title": "Certainty for Our Energy Future Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-18T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Certainty for Our Energy Future Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to terminate the clean electricity production credit and clean electricity investment credit with respect to certain technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:33:34Z"
    }
  ]
}
```
