# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3286?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3286
- Title: Veterans Appeals Improvement and Modernization Act 2.0
- Congress: 119
- Bill type: S
- Bill number: 3286
- Origin chamber: Senate
- Introduced date: 2025-12-01
- Update date: 2026-05-07T16:21:21Z
- Update date including text: 2026-05-07T16:21:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in Senate
- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-12-01: Introduced in Senate

## Actions

- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3286",
    "number": "3286",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Veterans Appeals Improvement and Modernization Act 2.0",
    "type": "S",
    "updateDate": "2026-05-07T16:21:21Z",
    "updateDateIncludingText": "2026-05-07T16:21:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
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
        "item": [
          {
            "date": "2026-04-29T21:37:14Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-01T23:34:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3286is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3286\nIN THE SENATE OF THE UNITED STATES\nDecember 1, 2025 Mr. Cassidy (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve processes relating to appeals of decisions regarding claims for benefits under the laws administered by the Secretary of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Appeals Improvement and Modernization Act 2.0 .\n#### 2. Improvements to processes relating to appeals of decisions regarding claims for benefits under the laws administered by the Secretary of Veterans Affairs\n##### (a) Evidentiary docket\nSubsection (c) of section 7113 is amended to read as follows:\n(c) Cases with no request for a hearing and with a request for additional evidence For cases in which a hearing is not requested in the notice of disagreement but an opportunity to submit evidence is requested, the evidentiary record before the Board shall be limited to evidence submitted by the appellant and his or her representative, if any, at any time before the date that is 90 days following receipt of the notice of disagreement. .\n##### (b) Hearing docket\nSubsection (b) of such section is amended to read as follows:\n(b) Cases with a request for a hearing For cases in which a hearing is requested in the notice of disagreement, the evidentiary record before the Board shall be limited to evidence submitted by the appellant and his or her representative, if any, at any time before the date that is 90 days following the Board hearing. .\n##### (c) Docket flexibility\nSection 7107(e) of such title is amended\u2014\n**(1)**\nby inserting (1) before The Secretary ; and\n**(2)**\nby adding at the end the following new paragraphs:\n(2) The Secretary shall develop and implement a policy allowing an appellant to withdraw an appeal in the appellant's case by filing a supplemental claim to the agency of original jurisdiction at any time without losing continuous pursuit in cases in which\u2014 (A) the appellant has not submitted new evidence for the case or the case has not had a Board hearing; and (B) the case has not been decided by the Board. (3) The Secretary\u2019s policy developed and implemented under paragraph (1) shall allow the appellant to move the appellant's case from one docket to another docket at any time without losing continuous pursuit in cases in which\u2014 (A) the appellant has not submitted new evidence for the case or the case has not had a Board hearing; and (B) the case has not been decided by the Board. .\n#### 3. Electronic notices by Board of Veterans' Appeals of decisions on appeal\nSection 7104(f) of title 38, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking if and inserting unless ; and\n**(B)**\nby inserting in a manner other than after such notice ; and\n**(2)**\nin paragraph (2), by inserting make or before revoke .\n#### 4. Requirements for notices by Board of Veterans' Appeals regarding decisions of the Board\nSection 7104(d)(1) of title 38, United States Code, is amended by striking record; and inserting the following: \u201crecord, including\u2014\n(A) identification of the issues adjudicated; (B) a summary of the evidence considered by the Board; (C) a summary of the applicable laws and regulations; (D) identification of findings favorable to the claimant; (E) in the case of a denial, identification of elements not satisfied leading to the denial; (F) an explanation of how to obtain or access evidence used in making the decision; and (G) if applicable, identification of the criteria that must be satisfied to grant service connection or the next higher level of compensation; .\n#### 5. Plan for veterans benefits management system and caseflow integration\n##### (a) Review\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall complete a review of the electronic systems used to process appeals under chapter 71 of title 38, United States Code.\n##### (b) Plan\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to the Committee on Veterans' Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives a plan to ensure the following:\n**(1)**\nSeamless integration between systems used to process decision at agencies of jurisdiction and the systems used by the Board of Veterans' Appeals to process appeals for benefits under title 38, United States Code.\n**(2)**\nLife-cycle tracking of appeals of decisions regarding assistance or support services under section 1720G of title 38, United States Code.\n#### 6. Reconsideration of decisions of Board of Veterans' Appeals\nSection 7103 of title 38, United States Code, is amended to read as follows:\n7103. Reconsideration; correction of obvious errors (a) Orders of the Chairman (1) The decision of the Board determining a matter under section 7102 of this title is final unless the Chairman orders reconsideration of the decision in accordance with paragraph (2). Such an order may be made on the Chairman\u2019s initiative or upon motion of the claimant. (2) (A) Upon the order of the Chairman for reconsideration of the decision in a case, the case shall be referred\u2014 (i) in the case of a matter originally decided by a single member of the Board, to a panel of not less than three members of the Board; or (ii) in the case of a matter originally decided by a panel of members of the Board, to an enlarged panel of the Board. (B) A panel referred to in subparagraph (A) may not include the member, or any member of the panel, that made the decision subject to reconsideration. (C) A panel reconsidering a case under this subsection shall render its decision after reviewing the entire record before the Board. The decision of the panel shall be made by a majority vote of the members of the panel. The decision of the panel shall constitute the final decision of the Board. (b) Correction of obvious errors The Board on its own motion may correct an obvious error in the record, without regard to whether there has been a motion or order for reconsideration. (c) Motion of claimant (1) (A) A claimant may submit to the Board a motion requesting a review of the decision of a member of the Board by a different member or panel of members of the Board. (B) The Chairman shall approve each request for review under subparagraph (A). (2) A request for higher-level review by the Board shall be\u2014 (A) in writing in such form as the Secretary may prescribe; and (B) made within the timeframe given to appeal a decision of the Board. (3) Notice of a decision under this subsection shall be provided to the claimant (and any representative of such claimant) and shall include a general statement\u2014 (A) reflecting whether evidence was not considered pursuant to paragraph (4); and (B) noting the options available to the claimant to have the evidence described in subparagraph (A), if any, considered by the Department. (4) The evidentiary record before a member of the Board shall be limited to the evidence of record in the Board decision being reviewed. (5) A reconsideration of a decision under this subsection shall be de novo. .\n#### 7. Order of decision of Board of Veterans' Appeals\nSection 7107 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(4), by striking in subsection (b) and inserting in subsection (b) or (c)(3) ; and\n**(2)**\nin subsection (c), by adding at the end the following new paragraph:\n(3) At the discretion of the member of the Board conducting a hearing, the Board may issue a decision, in whole or in part, during the hearing. .\n#### 8. Annual report on outcomes of appeals\n##### (a) In general\nSubchapter I of chapter 51 of title 38, United States Code, is amended by adding at the end the following new section:\n5109C. Annual report on outcomes of appeals (a) In general Not less frequently than once each year, the Secretary shall submit to Congress and publish on an internet website of the Department a report on the outcome of appeals, including with respect to supplemental review, higher-level review, and options for appeals to the Board of Veterans' Appeals. (b) Disaggregation of data The information reported and published pursuant to subsection (a) shall be disaggregated by the following: (1) Type of review. (2) Agency of original jurisdiction. (3) Nature of issue, such as service connection, disability rating, or effective date. (4) Body system or diagnostic code. (5) Outcome, such as affirmed or reversed, benefit awarded, remand for medical opinion, remand to obtain records, or remand for other reason. (c) Deidentified The Secretary shall insure that all information published under this section is deidentified. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 51 of such title is amended by inserting after the item relating to section 5109B the following new item:\n5109C. Annual report on outcomes of appeals. .\n#### 9. Third-party review of Department of Veterans Affairs appeals process\n##### (a) In general\nThe Secretary of Veterans Affairs shall seek to enter into an agreement with a non-Department of Veterans Affairs entity that the Secretary determines has knowledge of the appeals process of the Department of Veterans Affairs and the Federal rules of appellate procedures to carry out a review of such process.\n##### (b) Period for entering into agreement\nThe Secretary shall seek to enter into the agreement described in subsection (a) before the date that is 180 days after the date of the enactment of this Act.\n##### (c) Elements\nPursuant to an agreement entered into by the Secretary and an entity under subsection (a), the entity shall conduct the review covered by the agreement, including the following:\n**(1)**\nA review of joint motions for remand appeals decisions made by the Board of Veterans' Appeals.\n**(2)**\nA review of remands by the Board of decisions made by agencies of original jurisdiction.\n**(3)**\nDevelopment of recommendations for legislative or administrative action to increase the quality of decisions made by agencies of original jurisdiction and the Board of Veterans' Appeals, and reduce the prevalence of remands.\n#### 10. Comptroller General of the United States review of precedent setting decisions of United States Court of Appeals for Veterans Claims and Office of the General Counsel\n##### (a) Review\nThe Comptroller General of the United States shall conduct a review of the implementation by the Department of Veterans Affairs of precedential decisions issues by the United States Court of Appeals for Veterans Claims or the Office of the General Counsel of the Department of Veterans Affairs.\n##### (b) Elements\nThe review conducted under subsection (a) shall cover the following:\n**(1)**\nThe circumstances in which the Court or Office issued precedential decisions and factors which may limit the ability of the Court or Office to issue such decisions.\n**(2)**\nThe process of the Department for providing training and guidance for claims processors and how that process affects compliance with precendential decisions described in subsection (a).\n**(3)**\nAccuracy of claims decisions when applying new precedent.\n**(4)**\nWhether the structure or type of precedential decision affects the implementation by the Department.\n**(5)**\nPerspectives of stakeholders with respect to training, guidance, and quality assurance at the Department.\n**(6)**\nSuch other matters relating to challenges and opportunities for improvement relating to precedential decisions as the Comptroller General considers appropriate.\n##### (c) Report\nNot later than two years after the date of the enactment of this Act, the Comptroller General shall submit to the Committee on Veterans' Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives a report on the findings of the Comptroller General with respect to the review conducted under subsection (a).",
      "versionDate": "2025-12-01",
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
            "name": "Advisory bodies",
            "updateDate": "2026-05-07T16:09:28Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-07T16:20:35Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-05-07T16:13:08Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2026-05-07T16:20:55Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-05-07T16:21:21Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2026-05-07T16:03:22Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2026-05-07T15:57:54Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2026-05-07T15:57:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T16:19:47Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3286is.xml"
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
      "title": "Veterans Appeals Improvement and Modernization Act 2.0",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Appeals Improvement and Modernization Act 2.0",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to improve processes relating to appeals of decisions regarding claims for benefits under the laws administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T06:18:25Z"
    }
  ]
}
```
