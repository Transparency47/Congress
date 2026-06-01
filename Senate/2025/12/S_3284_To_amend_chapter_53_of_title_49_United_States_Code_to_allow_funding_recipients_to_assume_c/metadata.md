# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3284?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3284
- Title: Streamline Transit Projects Act
- Congress: 119
- Bill type: S
- Bill number: 3284
- Origin chamber: Senate
- Introduced date: 2025-12-01
- Update date: 2026-01-12T20:36:37Z
- Update date including text: 2026-01-12T20:36:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in Senate
- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-01: Introduced in Senate

## Actions

- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3284",
    "number": "3284",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Streamline Transit Projects Act",
    "type": "S",
    "updateDate": "2026-01-12T20:36:37Z",
    "updateDateIncludingText": "2026-01-12T20:36:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-12-01",
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
          "date": "2025-12-01T21:34:32Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "UT"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "AZ"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3284is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3284\nIN THE SENATE OF THE UNITED STATES\nDecember 1, 2025 Mr. Lee (for himself, Mr. Curtis , Mr. Kelly , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend chapter 53 of title 49, United States Code, to allow funding recipients to assume certain responsibilities relating to the National Environmental Policy Act of 1969.\n#### 1. Short title\nThis Act may be cited as the Streamline Transit Projects Act .\n#### 2. NEPA reform for categorical exclusions\n##### (a) In general\nChapter 53 of title 49, United States Code, is amended by inserting after section 5321 the following:\n5322. Transit agency assumption of responsibility for categorical exclusions (a) Definition In this section, the term eligible recipient means a direct recipient of funds under this chapter that\u2014 (1) is located in an urbanized area with a population of more than 200,000 individuals; and (2) demonstrates to the Secretary that the recipient has the legal, technical, and financial capacity to perform the responsibilities required under this section. (b) Categorical exclusion determinations (1) In general The Secretary may assign to an eligible recipient, and an eligible recipient may assume, responsibility for determining whether certain designated activities are included within classes of action identified by the Secretary that are categorically excluded from requirements for environmental assessments or environmental impact statements pursuant to the interim final rule promulgated by the Secretary at part 771 of title 23, Code of Federal Regulations, or any successor regulation. (2) Scope of authority A determination described in paragraph (1)\u2014 (A) shall be made by an eligible recipient in accordance with criteria established by the Secretary; and (B) may only be made by an eligible recipient with respect to a type of activity under this chapter specifically designated by the Secretary. (3) Criteria The criteria under paragraph (2)(A) shall include provisions for public availability of information consistent with section 552 of title 5 and the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ). (4) Preservation of flexibility The Secretary may not require an eligible recipient, as a condition of assuming responsibility under this section, to forego project delivery methods that are otherwise permissible for transit projects. (c) Other applicable Federal laws (1) In general If an eligible recipient assumes responsibility under subsection (b), the Secretary may also assign, and the eligible recipient may assume, all or part of the responsibilities of the Secretary for environmental review, consultation, or other related actions required under any Federal law applicable to activities that are classified by the Secretary as categorical exclusions, with the exception of government-to-government consultation with Indian Tribes, subject to the same procedural and substantive requirements as would be required if that responsibility were carried out by the Secretary. (2) Sole responsibility An eligible recipient that assumes responsibility under paragraph (1) with respect to a Federal law shall be solely responsible and solely liable for complying with and carrying out that law, and the Secretary shall have no such responsibility or liability. (d) Memoranda of understanding (1) In general The Secretary and an eligible recipient, after providing public notice and opportunity for comment, shall enter into a memorandum of understanding setting forth the responsibilities to be assigned under this section and the terms and conditions under which the assignments are made, including establishment of the circumstances under which the Secretary would reassume responsibility for categorical exclusion determinations. (2) Assistance Upon request by an eligible recipient, the Secretary shall provide to the eligible recipient technical assistance, training, or other support relating to\u2014 (A) assuming responsibility under subsection (b); (B) developing a memorandum of understanding under this subsection; or (C) addressing a responsibility in need of corrective action under subsection (e)(1)(B). (3) Term A memorandum of understanding under this subsection\u2014 (A) except as provided under subparagraph (C), shall have a term of not more than 3 years; (B) shall be renewable; and (C) for an eligible recipient that has assumed the responsibility for categorical exclusions under this section for a period of not less than 10 years, shall have a term of 5 years. (4) Acceptance of jurisdiction In a memorandum of understanding under this subsection, the eligible recipient shall consent to accept the jurisdiction of the Federal courts for the compliance, discharge, and enforcement of any responsibility of the Secretary that the eligible recipient assumes. (5) Monitoring The Secretary shall\u2014 (A) monitor\u2014 (i) compliance by an eligible recipient with the memorandum of understanding entered into by the eligible recipient under this subsection; and (ii) the provision by the eligible recipient of financial resources to carry out the memorandum of understanding; and (B) take into account the performance by the eligible recipient when considering renewal of the memorandum of understanding. (e) Termination (1) Termination by Secretary The Secretary may terminate the assignment of responsibilities to an eligible recipient under this section if\u2014 (A) the Secretary determines that the eligible recipient is not adequately carrying out the responsibilities assigned to the eligible recipient; (B) the Secretary provides to the eligible recipient\u2014 (i) a notification of the determination of noncompliance; (ii) a period of not less than 120 days to take such corrective action as the Secretary determines to be necessary to comply with the applicable agreement; and (iii) upon request by the chief executive officer of the eligible recipient, a detailed description of each responsibility in need of corrective action regarding an inadequacy identified under subparagraph (A); and (C) after the notification and period described in clauses (i) and (ii) of subparagraph (B), the eligible recipient fails to take satisfactory corrective action, as determined by the Secretary. (2) Termination by the eligible recipient An eligible recipient may terminate the assumption of responsibilities by the eligible recipient under this section\u2014 (A) by providing to the Secretary a notice not later than the date that is 90 days before the date of termination; and (B) subject to such terms and conditions as the Secretary may provide. (f) Recipient agency deemed To be Federal agency An eligible recipient that is assigned a responsibility under this section shall be deemed to be a Federal agency for the purposes of the Federal law under which the responsibility is exercised. (g) Legal fees An eligible recipient assuming 1 or more responsibilities of the Secretary under this section for a specific project may use funds apportioned to the eligible recipient under this chapter for attorney's fees directly attributable to eligible activities associated with the project. .\n##### (b) Conforming amendment\nThe table of sections for chapter 53 of title 49, United States Code, is amended by inserting after the item relating to section 5321 the following:\n5322. Transit agency assumption of responsibility for categorical exclusions. .",
      "versionDate": "2025-12-01",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-12-05",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "6491",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Streamline Transit Projects Act",
      "type": "HR"
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
        "updateDate": "2025-12-18T17:04:50Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3284is.xml"
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
      "title": "Streamline Transit Projects Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T06:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Streamline Transit Projects Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T06:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 53 of title 49, United States Code, to allow funding recipients to assume certain responsibilities relating to the National Environmental Policy Act of 1969.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T06:18:38Z"
    }
  ]
}
```
