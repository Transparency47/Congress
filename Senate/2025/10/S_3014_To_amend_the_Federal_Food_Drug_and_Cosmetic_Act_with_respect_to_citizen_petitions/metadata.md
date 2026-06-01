# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3014?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3014
- Title: Ensuring Timely Access to Generics Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3014
- Origin chamber: Senate
- Introduced date: 2025-10-16
- Update date: 2026-04-30T22:27:33Z
- Update date including text: 2026-04-30T22:27:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-16: Introduced in Senate
- 2025-10-16 - IntroReferral: Introduced in Senate
- 2025-10-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-10-16: Introduced in Senate

## Actions

- 2025-10-16 - IntroReferral: Introduced in Senate
- 2025-10-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-16",
    "latestAction": {
      "actionDate": "2025-10-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3014",
    "number": "3014",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Ensuring Timely Access to Generics Act of 2025",
    "type": "S",
    "updateDate": "2026-04-30T22:27:33Z",
    "updateDateIncludingText": "2026-04-30T22:27:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-16",
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
      "actionDate": "2025-10-16",
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
          "date": "2025-10-16T14:51:20Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-16",
      "state": "ME"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3014is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3014\nIN THE SENATE OF THE UNITED STATES\nOctober 16, 2025 Mrs. Shaheen (for herself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act with respect to citizen petitions.\n#### 1. Short title\nThis Act may be cited as the Ensuring Timely Access to Generics Act of 2025 .\n#### 2. Ensuring timely access to generics\nSection 505(q) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(q) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)(i), by inserting , 10.31, after 10.30 ;\n**(B)**\nin subparagraph (E)\u2014\n**(i)**\nby striking application and and inserting application or ;\n**(ii)**\nby striking If the Secretary and inserting the following:\n(i) In general If the Secretary ; and\n**(iii)**\nby striking the second sentence and inserting the following:\n(ii) Primary purpose of delaying (I) In general In determining whether a petition was submitted with the primary purpose of delaying an application, the Secretary may consider the following factors: (aa) Whether the petition was submitted in accordance with paragraph (2)(B), based on when the petitioner knew the relevant information relied upon to form the basis of such petition. (bb) When the petition was submitted in relation to when the petitioner reasonably should have known the relevant information relied upon to form the basis of such petition. (cc) Whether the petitioner has submitted multiple or serial petitions or supplements to petitions raising issues that reasonably could have been known to the petitioner at the time of submission of the earlier petition or petitions. (dd) Whether the petition was submitted close in time to a known, first date upon which an application under subsection (b)(2) or (j) of this section or section 351(k) of the Public Health Service Act could be approved. (ee) Whether the petition was submitted without relevant data or information in support of the scientific positions forming the basis of such petition. (ff) Whether the petition raises the same or substantially similar issues as a prior petition to which the Secretary has responded substantively already, including if the subsequent submission follows such response from the Secretary closely in time. (gg) Whether the petition requests changing the applicable standards that other applicants are required to meet, including requesting testing, data, or labeling standards that are more onerous or rigorous than the standards the Secretary has determined to be applicable to the listed drug, reference product, or petitioner\u2019s version of the same drug. (hh) The petitioner's record of submitting petitions to the Food and Drug Administration that have been determined by the Secretary to have been submitted with the primary purpose of delay. (ii) Other relevant and appropriate factors, which the Secretary shall describe in guidance. (II) Guidance The Secretary may issue or update guidance, as appropriate, to describe factors the Secretary considers in accordance with subclause (I). ;\n**(C)**\nby striking subparagraph (F);\n**(D)**\nby redesignating subparagraphs (G) through (I) as subparagraphs (F) through (H), respectively; and\n**(E)**\nin subparagraph (H), as so redesignated, by striking submission of this petition and inserting submission of this document ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby redesignating subparagraphs (A) through (C) as subparagraphs (C) through (E), respectively;\n**(B)**\nby inserting before subparagraph (C), as so redesignated, the following:\n(A) In general A person shall submit a petition to the Secretary under paragraph (1) before filing a civil action in which the person seeks to set aside, delay, rescind, withdraw, or prevent submission, review, or approval of an application submitted under subsection (b)(2) or (j) of this section or section 351(k) of the Public Health Service Act. Such petition and any supplement to such a petition shall describe all information and arguments that form the basis of the relief requested in any civil action described in the previous sentence. (B) Timely submission of citizen petition A petition and any supplement to a petition shall be submitted within 180 days after the person knew the information that forms the basis of the request made in the petition or supplement. ;\n**(C)**\nin subparagraph (C), as so redesignated\u2014\n**(i)**\nin the heading, by striking within 150 days ;\n**(ii)**\nin clause (i), by striking during the 150-day period referred to in paragraph (1)(F), ; and\n**(iii)**\nby amending clause (ii) to read as follows:\n(ii) on or after the date that is 151 days after the date of submission of the petition, the Secretary approves or has approved the application that is the subject of the petition without having made such a final decision. ;\n**(D)**\nby amending subparagraph (D), as so redesignated, to read as follows:\n(D) Dismissal of certain civil actions (i) Petition If a person files a civil action against the Secretary in which a person seeks to set aside, delay, rescind, withdraw, or prevent submission, review, or approval of an application submitted under subsection (b)(2) or (j) of this section or section 351(k) of the Public Health Service Act without complying with the requirements of subparagraph (A), the court shall dismiss without prejudice the action for failure to exhaust administrative remedies. (ii) Timeliness If a person files a civil action against the Secretary in which a person seeks to set aside, delay, rescind, withdraw, or prevent submission, review, or approval of an application submitted under subsection (b)(2) or (j) of this section or section 351(k) of the Public Health Service Act without complying with the requirements of subparagraph (B), the court shall dismiss with prejudice the action for failure to timely file a petition. (iii) Final response If a civil action is filed against the Secretary with respect to any issue raised in a petition timely filed under paragraph (1) in which the petitioner requests that the Secretary take any form of action that could, if taken, set aside, delay, rescind, withdraw, or prevent submission, review, or approval of an application submitted under subsection (b)(2) or (j) of this section or section 351(k) of the Public Health Service Act before the Secretary has taken final agency action on the petition within the meaning of subparagraph (C), the court shall dismiss without prejudice the action for failure to exhaust administrative remedies. ; and\n**(E)**\nin clause (iii) of subparagraph (E), as so redesignated, by striking as defined under subparagraph (2)(A) and inserting within the meaning of subparagraph (C) ; and\n**(3)**\nin paragraph (4)\u2014\n**(A)**\nby striking Exceptions in the paragraph heading and all that follows through This subsection does and inserting Exceptions.\u2014 This subsection does ;\n**(B)**\nby striking subparagraph (B); and\n**(C)**\nby redesignating clauses (i) and (ii) as subparagraphs (A) and (B), respectively, and adjusting the margins accordingly.",
      "versionDate": "2025-10-16",
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
        "actionDate": "2026-03-25",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4189",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "INSULIN Act of 2026",
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
        "name": "Health",
        "updateDate": "2025-12-08T16:27:45Z"
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
      "date": "2025-10-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3014is.xml"
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
      "title": "Ensuring Timely Access to Generics Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T11:18:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Timely Access to Generics Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act with respect to citizen petitions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:23Z"
    }
  ]
}
```
