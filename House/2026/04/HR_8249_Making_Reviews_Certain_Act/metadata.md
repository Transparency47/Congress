# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8249?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8249
- Title: Making Reviews Certain Act
- Congress: 119
- Bill type: HR
- Bill number: 8249
- Origin chamber: House
- Introduced date: 2026-04-13
- Update date: 2026-04-20T19:23:45Z
- Update date including text: 2026-04-20T19:23:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-13: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-04-13: Introduced in House

## Actions

- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-13",
    "latestAction": {
      "actionDate": "2026-04-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8249",
    "number": "8249",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Making Reviews Certain Act",
    "type": "HR",
    "updateDate": "2026-04-20T19:23:45Z",
    "updateDateIncludingText": "2026-04-20T19:23:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-13",
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
      "actionDate": "2026-04-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-13",
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
          "date": "2026-04-13T18:31:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8249ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8249\nIN THE HOUSE OF REPRESENTATIVES\nApril 13, 2026 Mr. Gottheimer introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the National Environmental Policy Act of 1969 to clarify the scope of review, establish limits for judicial review of environmental documents relating to energy infrastructure, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Making Reviews Certain Act .\n#### 2. Scope of review\nSection 106 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4336 ) is amended\u2014\n**(1)**\nin the heading, by inserting ; scope of review after level of review ; and\n**(2)**\nby adding at the end the following:\n(c) Scope of review In preparing an environmental document for a proposed agency action, a Federal agency is only required to consider those effects that share a reasonably close causal relationship to, and are proximately caused by, the immediate project or action under consideration, to comply with the requirements of this Act. .\n#### 3. Limitations on judicial review of environmental documents relating to energy infrastructure\nTitle I of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4331 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 112 as section 110A and moving such section so as to appear after section 110; and\n**(2)**\nby inserting before section 111 the following:\n110B. Limitations on judicial review of environmental documents relating to energy infrastructure (a) Limitations on claims (1) In general Notwithstanding any other provision of law (except as provided in subparagraph (A) with respect to a shorter deadline), a claim challenging whether a final agency action relating to energy infrastructure complies with the requirements of this Act shall be barred unless\u2014 (A) such claim is filed not later than 180 days after the final agency action is made public, unless a shorter deadline is specified under law; (B) in the case of a final agency action for which there was a public comment period on an environmental document, such claim\u2014 (i) is filed by a party that submitted a substantive and unique comment during such public comment period by the noticed comment deadline for the environmental document and such comment was sufficiently detailed to put the applicable Federal agency on notice of the issue upon which the party seeks review; and (ii) concerns the same subject matter raised in the comment submitted during the public comment period; (C) such claim is filed by a party that has suffered or imminently will suffer direct harm from the final agency action; and (D) such claim does not challenge the establishment of a categorical exclusion. (2) Energy infrastructure defined In this subsection, the term energy infrastructure means a facility, and associated equipment, used for enabling the identification, leasing, development, production, processing, transportation, transmission, refining, and generation needed for energy. (b) Limitations on remand (1) In general Notwithstanding any other provision of law, no final agency action shall be vacated by a court, following a decision on the merits, unless the court determines that\u2014 (A) the major Federal action for which the environmental document or final agency action is prepared will pose a significant risk of a proximate and substantial environmental harm; and (B) there is no other equitable remedy available as a matter of law. (2) Remand Notwithstanding any other provision of law, if a court determines there are errors or deficiencies with an environmental document or final agency action that need to be corrected\u2014 (A) the court may remand the environmental document to the applicable Federal agency with specific instruction to correct such errors or deficiencies within 180 days from the date on which the order of the court was issued to the applicable Federal agency; and (B) the major Federal action may be carried out pursuant to the final agency action notwithstanding the remand of the environmental document or final agency action under subparagraph (A), including during the time prescribed by the court to the Federal agency to correct such errors or deficiencies, so long as the court has not determined that vacatur is appropriate under paragraph (1). (c) No effect on review of compliance with other deadlines This section shall not affect the right to obtain review under section 107(g)(3). .\n#### 4. Deference to agencies in judicial review\nSection 111 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4336e ) is amended by adding at the end the following:\n(14) Reasonably foreseeable To comply with the requirements of this Act, the term reasonably foreseeable , with respect to environmental effects of a proposed agency action, means effects that share a reasonably close causal relationship to, and are proximately caused by, the immediate project or action under consideration. .",
      "versionDate": "2026-04-13",
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
        "updateDate": "2026-04-20T19:23:45Z"
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
      "date": "2026-04-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8249ih.xml"
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
      "title": "Making Reviews Certain Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T04:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Making Reviews Certain Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Environmental Policy Act of 1969 to clarify the scope of review, establish limits for judicial review of environmental documents relating to energy infrastructure, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T04:18:34Z"
    }
  ]
}
```
