# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/106?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/106
- Title: LIST Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 106
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-18T15:12:49Z
- Update date including text: 2025-02-18T15:12:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/106",
    "number": "106",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "LIST Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-18T15:12:49Z",
    "updateDateIncludingText": "2025-02-18T15:12:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:10:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr106ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 106\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Endangered Species Act of 1973 to provide for improved precision in the listing, delisting, and downlisting of endangered species and potentially endangered species.\n#### 1. Short title\nThis Act may be cited as the Less Imprecision in Species Treatment Act of 2025 or the LIST Act of 2025 .\n#### 2. Requirement to initiate delisting\n##### (a) Requirement in case of recovery\nSection 4(b) of the Endangered Species Act of 1973 ( 16 U.S.C. 1533(b) ) is amended by adding at the end the following:\n(9) (A) The Secretary shall initiate the procedures in accordance with subsection (a)(1) to remove a species from a list published under subsection (c) if\u2014 (i) the goals of a recovery plan for the species developed under subsection (f) have been met; or (ii) the goals for recovery of the species have not been developed under subsection (f), and the Secretary determines that the species has recovered sufficiently to no longer require the protection of the Act. (B) Notwithstanding the requirement of subsection (c)(2) that each determination under subparagraph (B) of that subsection shall be made in accordance with the provisions of subsections (a) and (b), the Secretary shall remove a species from any list published under subsection (c) if the Department of the Interior has produced or received substantial scientific or commercial information demonstrating that the species is recovered or that recovery goals set for the species under subsection (f) have been met. (C) In the case of a species removed under subparagraph (A) from a list published under subsection (c), the publication and notice under subsection (b)(5) shall consist solely of a notice of such removal. .\n##### (b) Requirement in case erroneously or wrongfully listed\nSection 4(b)(3) of the Endangered Species Act of 1973 ( 16 U.S.C. 1533(a) ), as amended by subsection (a), is further amended by adding at the end the following:\n(E) (i) Not later than 90 days after the date the Department of the Interior receives or produces under this subsection information described in clause (ii) regarding a species included in a list under subsection (c), the Secretary shall to the maximum extent practicable find whether the inclusion of such species in such list was less than likely to have occurred in the absence of the scientific or commercial information referred to in clause (ii). (ii) Information referred to in clause (i) is any information demonstrating that the listing was determined on the basis of scientific or commercial information available to, or received or produced by, the Department under paragraphs (1) and (3) of subsection (b) that at the time the scientific or commercial information was available to or received or produced by the Department it was\u2014 (I) inaccurate beyond scientifically reasonable margins of error; (II) fraudulent; or (III) misrepresentative. (iii) Notwithstanding the requirement under subsection (c)(2)(B) that each determination under subparagraph (B) shall be made in accordance with the provisions of subsections (a) and (b), the Secretary shall\u2014 (I) remove from any list published under subsection (c) any species for which a positive finding is made under clause (i); and (II) promptly publish in the Federal Register notice of such finding that includes such information as was received or produced by the Department under such clause. (iv) Any positive finding by the Secretary under clause (i) shall not be subject to judicial review. (v) Any negative finding by the Secretary under clause (i) shall be subject to judicial review. (vi) In the case of a species removed under clause (iii) from a list, the publication and notice under subsection (b)(5) shall consist solely of a notice of such removal. (vii) If the Secretary finds that a person submitted a petition that is the subject of a positive finding under clause (i) knowing that it contained scientific or commercial information described in clause (ii), then during the 10-year period beginning on the date of the finding under this clause the person shall not be considered an interested person for purposes of subparagraph (A) with respect to any petition submitted by the person after the date the person submitted such scientific or commercial information. .\n#### 3. Expanded consideration during 5-year review\nSection 4(c) of the Endangered Species Act of 1973 ( 16 U.S.C. 1533(c) ) is amended by adding at the end the following:\n(3) Each determination under paragraph (2)(B) shall consider one of the following: (A) Except as provided in subparagraph (B) of this paragraph, the criteria required under subsection (f)(1)(B) in the recovery plan for the species. (B) If the objective, measurable criteria under subsection (f)(1)(B)(ii) are not established, the factors for the determination that a species is an endangered species or a threatened species set forth in subsections (a)(1) and (b)(1). (C) A finding of error in the determination that the species is an endangered species, a threatened species, or extinct. (D) A determination that the species is no longer an endangered species or threatened species or in danger of extinction, based on an analysis of the factors that are the basis for listing in subsections (a)(1) and (b)(1). .",
      "versionDate": "2025-01-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-02-14T19:26:22Z"
          },
          {
            "name": "Administrative remedies",
            "updateDate": "2025-02-14T19:26:22Z"
          },
          {
            "name": "Department of the Interior",
            "updateDate": "2025-02-14T19:26:22Z"
          },
          {
            "name": "Endangered and threatened species",
            "updateDate": "2025-02-14T19:26:22Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-14T19:26:22Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-02-14T19:26:22Z"
          },
          {
            "name": "Scientific communication",
            "updateDate": "2025-02-14T19:26:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-02-03T15:30:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr106",
          "measure-number": "106",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr106v00",
            "update-date": "2025-02-18"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Less Imprecision in Species Treatment Act of 2025 or the LIST Act of 2025</strong></p><p>This bill modifies the process for removing a species from the endangered or threatened species lists and makes related requirements.\u00a0</p><p>A species must be removed from the endangered or threatened species lists if the U.S. Fish and Wildlife Service and the National Marine Fisheries Service produces or receives substantial scientific or commercial information demonstrating that the species is recovered or that recovery goals set for the species have been met.</p><p>The publication and notice of a proposed regulation to remove a species from the lists must consist solely of a notice of the removal.</p><p>The bill establishes a process for removing species from the lists if they were erroneously or wrongfully listed. The bill prohibits a person from submitting a petition to list a species as a threatened or endangered species for 10 years if the person knowingly submitted a petition with information that was inaccurate beyond scientifically reasonable margins of error, fraudulent, or misrepresentative.</p>"
        },
        "title": "LIST Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr106.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Less Imprecision in Species Treatment Act of 2025 or the LIST Act of 2025</strong></p><p>This bill modifies the process for removing a species from the endangered or threatened species lists and makes related requirements.\u00a0</p><p>A species must be removed from the endangered or threatened species lists if the U.S. Fish and Wildlife Service and the National Marine Fisheries Service produces or receives substantial scientific or commercial information demonstrating that the species is recovered or that recovery goals set for the species have been met.</p><p>The publication and notice of a proposed regulation to remove a species from the lists must consist solely of a notice of the removal.</p><p>The bill establishes a process for removing species from the lists if they were erroneously or wrongfully listed. The bill prohibits a person from submitting a petition to list a species as a threatened or endangered species for 10 years if the person knowingly submitted a petition with information that was inaccurate beyond scientifically reasonable margins of error, fraudulent, or misrepresentative.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr106"
    },
    "title": "LIST Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Less Imprecision in Species Treatment Act of 2025 or the LIST Act of 2025</strong></p><p>This bill modifies the process for removing a species from the endangered or threatened species lists and makes related requirements.\u00a0</p><p>A species must be removed from the endangered or threatened species lists if the U.S. Fish and Wildlife Service and the National Marine Fisheries Service produces or receives substantial scientific or commercial information demonstrating that the species is recovered or that recovery goals set for the species have been met.</p><p>The publication and notice of a proposed regulation to remove a species from the lists must consist solely of a notice of the removal.</p><p>The bill establishes a process for removing species from the lists if they were erroneously or wrongfully listed. The bill prohibits a person from submitting a petition to list a species as a threatened or endangered species for 10 years if the person knowingly submitted a petition with information that was inaccurate beyond scientifically reasonable margins of error, fraudulent, or misrepresentative.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr106"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr106ih.xml"
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
      "title": "LIST Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LIST Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T11:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Less Imprecision in Species Treatment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T11:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Endangered Species Act of 1973 to provide for improved precision in the listing, delisting, and downlisting of endangered species and potentially endangered species.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T11:03:22Z"
    }
  ]
}
```
