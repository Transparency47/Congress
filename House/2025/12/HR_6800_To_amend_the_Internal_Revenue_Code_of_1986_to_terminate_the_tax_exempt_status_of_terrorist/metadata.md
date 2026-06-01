# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6800?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6800
- Title: To amend the Internal Revenue Code of 1986 to terminate the tax-exempt status of terrorist supporting organizations.
- Congress: 119
- Bill type: HR
- Bill number: 6800
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-01-22T17:47:10Z
- Update date including text: 2026-01-22T17:47:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6800",
    "number": "6800",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000392",
        "district": "8",
        "firstName": "David",
        "fullName": "Rep. Kustoff, David [R-TN-8]",
        "lastName": "Kustoff",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to terminate the tax-exempt status of terrorist supporting organizations.",
    "type": "HR",
    "updateDate": "2026-01-22T17:47:10Z",
    "updateDateIncludingText": "2026-01-22T17:47:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:06:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6800ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6800\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mr. Kustoff introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to terminate the tax-exempt status of terrorist supporting organizations.\n#### 1. Termination of tax-exempt status of terrorist supporting organizations\n##### (a) In general\nSection 501(p) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(8) Application to terrorist supporting organizations (A) In general For purposes of this subsection, in the case of any terrorist supporting organization\u2014 (i) such organization (and the designation of such organization under subparagraph (B)) shall be treated as described in paragraph (2), and (ii) the period of suspension described in paragraph (3) with respect to such organization shall be treated as beginning on the date that the Secretary designates such organization under subparagraph (B) and ending on the date that the Secretary rescinds such designation under subparagraph (D). (B) Terrorist supporting organization For purposes of this paragraph\u2014 (i) In general the term terrorist supporting organization means any organization which is designated by the Secretary as having provided, during the 3-year period ending on the date of such designation, material support or resources to an organization described in paragraph (2) (determined after the application of this paragraph to such organization) in excess of a de minimis amount. (ii) Material support or resources The term material support or resources has the meaning given such term in subsection (g)(4) of section 2339B of title 18, United States Code, except that such term shall not include\u2014 (I) support or resources that were approved by the Secretary of State with the concurrence of the Attorney General for purposes of subsection (j) of such section, or (II) humanitarian aid provided with the approval of the Office of Foreign Assets Control. (C) Designation procedure (i) Notice requirement Prior to designating any organization as a terrorist supporting organization under subparagraph (B), the Secretary shall mail to the most recent mailing address provided by such organization on the organization\u2019s annual return or notice under section 6033 (or subsequent form indicating a change of address) a written notice which includes\u2014 (I) a statement that the Secretary will designate such organization as a terrorist supporting organization unless the organization satisfies the requirements of subclause (I) or (II) of clause (ii), (II) the name of the organization or organizations with respect to which the Secretary has determined such organization provided material support or sources as described in subparagraph (B), (III) a description of such material support or resources except to the extent that the Secretary determines that disclosure of such description would be inconsistent with national security or law enforcement interests, and (IV) if the Secretary makes the determination described in subclause (III), a statement that the Secretary has made such determination and that all or part of the description of such material support or resources is not included in such notice by reason of such determination. (ii) Opportunity to cure In the case of any notice provided to an organization under clause (i), the Secretary shall, at the close of the 90-day period beginning on the date that such notice was sent, designate such organization as a terrorist supporting organization under subparagraph (B) if (and only if) such organization has not (during such period)\u2014 (I) demonstrated to the satisfaction of the Secretary that such organization did not provide the material support or resources referred to in subparagraph (B), (II) made reasonable efforts to have such support or resources returned to such organization and certified in writing to the Secretary that such organization will not provide any further support or resources to organizations described in paragraph (2), or (III) if such notice included a statement described in clause (i)(IV), filed a complaint with a United States district court of competent jurisdiction alleging that Secretary\u2019s determination under clause (i)(III) is erroneous. A certification under subclause (II) shall not be treated as valid if the organization making such certification has provided any other such certification during the preceding 5 years. (iii) Application of opportunity to cure following complaint regarding determination to withhold description of material support or resources In the case of a final judgment of a court of competent jurisdiction that the Secretary\u2019s determination under clause (i)(III) was not erroneous, clause (ii) shall be applied without regard to subclause (III) thereof and as though the notice referred to in such clause was sent on the first date that all rights of appeal with respect to such final judgement have concluded. (D) Rescission The Secretary shall rescind a designation under subparagraph (B) if (and only if)\u2014 (i) the Secretary determines that such designation was erroneous, (ii) after the Secretary receives a written certification from an organization that such organization did not receive the notice described in subparagraph (C)(i)\u2014 (I) the Secretary determines that it is reasonable to believe that such organization did not receive such notice, and (II) such organization satisfies the requirements of subclause (I) or (II) of subparagraph (C)(ii) (determined after taking into account the last sentence thereof), or (iii) the Secretary determines, with respect to all organizations to which the material support or resources referred to in subparagraph (B) were provided, the periods of suspension under paragraph (3) have ended. A certification described in the matter preceding subclause (I) of clause (ii) shall not be treated as valid if the organization making such certification has provided any other such certification during the preceding 5 years. (E) Administrative review by Internal Revenue Service Independent Office of Appeals In the case of the designation of an organization by the Secretary as a terrorist supporting organization under subparagraph (B), a dispute regarding such designation shall be subject to resolution by the Internal Revenue Service Independent Office of Appeals under section 7803(e) in the same manner as if such designation were made by the Internal Revenue Service and paragraph (5) of this subsection did not apply. (F) Jurisdiction of United States courts Notwithstanding paragraph (5), the United States district courts shall have exclusive jurisdiction to review any determination of the Secretary under subparagraph (C)(i)(III) and any final determination with respect to an organization\u2019s designation as a terrorist supporting organization under subparagraph (B). In the case of any such determination which was based on classified information (as defined in section 1(a) of the Classified Information Procedures Act), such information may be submitted to the reviewing court ex parte and in camera. For purposes of this subparagraph, a determination with respect to an organization\u2019s designation as a terrorist supporting organization shall not fail to be treated as a final determination merely because such organization fails to utilize the dispute resolution process of the Internal Revenue Service Independent Office of Appeals provided under subparagraph (E). (G) Classified information The Secretary shall establish policies and procedures for purposes of this paragraph that ensure that employees of the Department of the Treasury comply with all laws regarding the handling and review of classified information (as defined in section 1(a) of the Classified Information Procedures Act). .\n##### (b) Effective date\nThe amendment made by this section shall apply to designations made after the date of the enactment of this Act in taxable years ending after such date.",
      "versionDate": "2025-12-17",
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
        "actionDate": "2025-12-17",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3554",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to amend the Internal Revenue Code of 1986 to terminate the tax-exempt status of terrorist supporting organizations.",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-04",
        "text": "Became Public Law No: 119-21."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "An act to provide for reconciliation pursuant to title II of H. Con. Res. 14.",
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
        "name": "Taxation",
        "updateDate": "2026-01-21T16:02:27Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6800ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to terminate the tax-exempt status of terrorist supporting organizations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:33:37Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to terminate the tax-exempt status of terrorist supporting organizations.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T09:06:56Z"
    }
  ]
}
```
