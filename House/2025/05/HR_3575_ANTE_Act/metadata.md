# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3575?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3575
- Title: ANTE Act
- Congress: 119
- Bill type: HR
- Bill number: 3575
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-12-05T22:54:39Z
- Update date including text: 2025-12-05T22:54:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3575",
    "number": "3575",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "ANTE Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:54:39Z",
    "updateDateIncludingText": "2025-12-05T22:54:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
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
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:01:20Z",
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
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "UT"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "TX"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "FL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "SC"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3575ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3575\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Arrington (for himself, Mr. Moore of Utah , Ms. Van Duyne , and Mr. Steube ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Trade Act of 1974 to authorize the United States Trade Representative to impose remedial measures with respect to certain entities that evade or may attempt to evade duties imposed with respect to nonmarket economy countries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Axing Nonmarket Tariff Evasion Act or the ANTE Act .\n#### 2. Imposition by Trade Representative of remedial measures in case of evasion of duties by certain entities of nonmarket economy countries\n##### (a) In general\nTitle III of the Trade Act of 1974 ( 19 U.S.C. 2411 et seq. ) is amended by adding at the end the following:\n311. Remedial measures regarding evasion of duties by certain entities of nonmarket economy countries (a) Inquiry The Trade Representative may initiate an inquiry into whether a covered entity is establishing, planning to establish, or has established an investment in a third country that would avoid duties imposed under section 301 with respect to a nonmarket economy country. (b) Remedial measures (1) In general If the Trade Representative makes an affirmative determination under subsection (a) with respect to a covered entity and the investment of that covered entity in a third country, the Trade Representative, subject to the specific direction, if any, of the President, may impose a remedial measure with respect to goods produced in the third country by a covered entity, which may include the imposition of a duty equal to not less than the value of the duty placed on the relevant product of the nonmarket economy country under section 301. (2) Timing An action under paragraph (1) may be taken with respect to a covered entity\u2014 (A) at any point during an investigation under section 301 if the third-country investment of the covered entity has begun production; and (B) prospectively, if the covered entity has plans to establish production in the third country. (c) Matters relating to inquiries (1) In general An inquiry under subsection (a) may be self-initiated by the Trade Representative or may be requested by interested persons (as defined in section 301(d)(9)) or Congress. (2) Initiation (A) In general If an inquiry is requested under paragraph (1) and the Trade Representative determines there is a reasonable indication that a covered entity is establishing, planning to establish, or has already established an investment in a third country that would avoid duties imposed under section 301 with respect to a nonmarket economy country, the Trade Representative may initiate an inquiry under subsection (a). (B) Information from other agencies Upon request of the Trade Representative, the head of a Federal agency shall submit to the Trade Representative any relevant information of the agency that is necessary for the Trade Representative to carry out an inquiry under subsection (a). (3) Determination To initiate inquiry Not later than 45 days after receipt of a request under paragraph (1), the Trade Representative shall determine whether an inquiry under subsection (a) is warranted. (4) Determination of evasion Not later than 180 days after a determination under paragraph (3) that an inquiry under subsection (a) is warranted with respect to a covered entity, the Trade Representative shall make an affirmative determination of duty evasion if it is found that the third-country investment\u2014 (A) is being established or acquired, or has been established or acquired, by the covered entity; and (B) is producing or planning to produce a good subject to a duty under section 301. (d) Additional measures (1) In general Based on the findings of an inquiry under subsection (a) with respect to a covered entity, the Trade Representative may, at the specific direction, if any, of the President, unilaterally impose a measure\u2014 (A) with respect to the covered entity; and (B) with respect to goods produced in a third country pursuant to the investment of that covered entity in the third country. (2) Timing A measure may be imposed under paragraph (1) with respect to a covered entity\u2014 (A) if the covered entity has begun production; or (B) prospectively, if the covered entity has immediate plans to establish production in the third country. (3) Decision not to impose a measure If the Trade Representative does not impose a measure under paragraph (1) with respect to a covered entity, the Trade Representative shall submit to Congress a justification as to why such a measure was not imposed, which shall include a description of the social and economic impacts of not imposing the measure. (4) Duration of measure If a measure is imposed by the Trade Representative under paragraph (1) with respect to a covered entity, the measure shall last as long as the remedial action with respect to the relevant nonmarket economy country imposed under section 301 remains in effect, or as long as the relevant nonmarket economy country has a controlling interest in the third-country investment of the covered entity, whichever terminates sooner. (e) Definitions In this section: (1) Control The term control has the meaning given that term in section 800.208 of title 31, Code of Federal Regulations (as in effect on the date of the enactment of this section). (2) Covered entity The term covered entity \u2014 (A) means an entity owned, controlled, subject to the jurisdiction or direction of, or operated by a nonmarket economy country; and (B) includes any entity for which, on any date during the most recent 12-month period, not less than 25 percent of the equity interests in that entity are held directly or indirectly by one or more entities organized under the laws of a nonmarket economy country, including through\u2014 (i) interests in co-investment vehicles, joint ventures, or similar arrangements; or (ii) a derivative financial instrument or contractual arrangement between the entity and a nonmarket economy country, including any such instrument or contract that seeks to replicate any financial return with respect to such entity or interest in such entity. (3) Nonmarket economy country The term nonmarket economy country means any country that is both\u2014 (A) determined to be a nonmarket economy country under section 771(18) of the Tariff Act of 1930 ( 19 U.S.C. 1677(18) ); and (B) included on the priority watch list, as defined in section 182(g)(3) (commonly known as the Special 301 Priority Watch List ). (4) Trade Representative The term Trade Representative means the United States Trade Representative. .\n##### (b) Clerical amendment\nThe table of contents for the Trade Act of 1974 is amended by inserting after the item relating to section 310 the following:\nSec. 311. Remedial measures regarding evasion of duties by certain entities in nonmarket economy countries. .",
      "versionDate": "2025-05-23",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1886",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ANTE Act",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-06-23T17:48:56Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3575ih.xml"
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
      "title": "ANTE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ANTE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Axing Nonmarket Tariff Evasion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Trade Act of 1974 to authorize the United States Trade Representative to impose remedial measures with respect to certain entities that evade or may attempt to evade duties imposed with respect to nonmarket economy countries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:35Z"
    }
  ]
}
```
