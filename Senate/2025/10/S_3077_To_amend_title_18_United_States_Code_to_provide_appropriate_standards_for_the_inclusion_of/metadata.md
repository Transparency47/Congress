# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3077?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3077
- Title: Safer Supervision Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3077
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2025-12-05T22:02:11Z
- Update date including text: 2025-12-05T22:02:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3077",
    "number": "3077",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "Safer Supervision Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:02:11Z",
    "updateDateIncludingText": "2025-12-05T22:02:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-30",
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
          "date": "2025-10-30T16:18:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "DE"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "MS"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "ND"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "NC"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3077is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3077\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Lee (for himself, Mr. Coons , Mr. Wicker , Mr. Cramer , Mr. Tillis , and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to provide appropriate standards for the inclusion of a term of supervised release after imprisonment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safer Supervision Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOver 110,000 people were on Federal supervised release as of December 2024.\n**(2)**\nThe Supreme Court of the United States explained in Johnson v. United States that Supervised release departed from the parole system it replaced by giving district courts the freedom to provide postrelease supervision for those, and only those, who needed it. ... Congress aimed, then, to use the district courts\u2019 discretionary judgment to allocate supervision to those releasees who needed it most. .\n**(3)**\nFederal probation officers report significant caseloads that can exceed 100 cases per officer. This can create a difficult burden for the officers and limit their ability to provide appropriate supervision to those who need it.\n**(4)**\nThe potential for early termination or other modifications of supervision, when consistent with public safety, can not only reduce burdens and save valuable judicial resources but also create positive incentives for compliance and rehabilitation consistent with the purposes of supervision. Requests for early termination and appeals from the denial of early termination are not challenges to the original sentence but rather an integral part of the rehabilitative scheme established by Congress. In the 12-month period ending in December 2024, early terminations were 29 percent of successful supervised release closures.\n**(5)**\nThe Administrative Office of the United States Courts has explained that excessive correctional intervention for low-risk defendants may increase the probability of recidivism by disrupting prosocial activities and exposing defendants to antisocial associates. .\n**(6)**\nSupervised release is and should remain an important tool for the Federal courts to use, as appropriate, to, among other items, protect the public from further crimes, deter future criminal conduct, and help the defendant become a contributing member of society by recovering from substance use disorder, participating in rehabilitation and training programs, and providing restitution to victims, among other outcomes.\n**(7)**\nBetter tailoring when and how supervised release is imposed, encouraging early termination when appropriate, and expanding judicial discretion on certain revocations will reduce burdens on law enforcement officers and taxpayers, encourage compliance and improve public safety, and better assist defendants in their pursuit of rehabilitation and reintegration, to the benefit of themselves, victims, and communities.\n#### 3. Inclusion of a term of supervised release after imprisonment\nSection 3583 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking The court and inserting the following:\n(1) In general The court ; and\n**(B)**\nby adding at the end the following:\n(2) Individualized assessment When determining whether to include a term of supervised release as part of the sentence, and except to the extent that a term of supervised release is required by statute as described in paragraph (1), the court shall\u2014 (A) make an individualized assessment under the factors set forth in subsections (c) and (d) as to\u2014 (i) whether such a term is appropriate; and (ii) the appropriate length and conditions of such a term; and (B) provide the reasons of the court for imposing or not imposing such a term on the record. ;\n**(2)**\nin subsection (d), in the fifth sentence, by striking shall also and inserting may also ;\n**(3)**\nin subsection (e)\u2014\n**(A)**\nby redesignating paragraphs (1) through (4) as subparagraphs (A) through (D), respectively, and adjusting the margins accordingly;\n**(B)**\nby striking The court may, and inserting the following:\n(1) In general Subject to paragraph (2), the court may, ;\n**(C)**\nin subparagraph (A), as so redesignated, by striking after the expiration of one year of supervised release ;\n**(D)**\nin subparagraph (C), as so redesignated, by striking this paragraph and inserting this subparagraph ;\n**(E)**\nin subparagraph (D), as so redesignated, by striking this paragraph and inserting this subparagraph ; and\n**(F)**\nby adding at the end the following:\n(2) Termination of supervised release For purposes of the termination of supervised release under paragraph (1)(A)\u2014 (A) after a defendant has served the lesser of 1 year of supervised release or 50 percent of the term of supervised release imposed on the defendant, the Administrative Office of the United States Courts shall provide notice to a defendant, defendant\u2019s counsel, and any local Federal Public Defender Organization or Community Defender Organization of the opportunity to seek early termination of supervised release under paragraph (1)(A) and the process for doing so; (B) there shall be a presumption of early termination of supervised release for a defendant under supervision if\u2014 (i) (I) for a defendant serving a term of supervised release imposed in connection with a conviction for an offense described in subsection (a) of section 16, the defendant has served 66.6 percent of the term of supervised release imposed on the defendant; or (II) for a defendant other than a defendant described in subclause (I), the defendant has served 50 percent of the term of supervised release imposed on the defendant; (ii) the defendant has demonstrated good conduct and compliance while on supervised release; and (iii) the early termination will not jeopardize public safety; (C) the Government shall have an opportunity to object to a request for termination of supervised release and to present evidence, which the defendant shall have the opportunity to rebut, in any proceeding relating to such request; and (D) crime victims\u2019 rights under section 3771 shall apply to any proceeding relating to a request for early termination of supervised release. (3) Public safety In assessing whether early termination of supervised release will not jeopardize public safety under this subsection, the court shall consider the nature of the offense committed by the defendant, the defendant\u2019s criminal history, the defendant\u2019s record while incarcerated (including good behavior and violations of prison rules), the defendant\u2019s efforts to avoid recidivism, the defendant\u2019s health status, any statements or information provided by victims of the offense, and other factors the court may find relevant to public safety. (4) Good conduct and compliance In assessing whether the defendant has demonstrated good conduct and compliance under this subsection, the court shall consider the defendant\u2019s efforts to reintegrate into the community and the defendant\u2019s substantial compliance with the conditions of supervision. (5) Assistance of counsel The court may appoint a Federal public defender, a community defender, or other counsel qualified to be appointed under section 3006A to assist a defendant seeking early termination of supervised release under paragraph (1)(A) or modification of conditions under paragraph (1)(B). (6) Rule of construction Paragraph (2)(B) shall not be construed to limit the discretion of a court under paragraph (1). (7) Clarification The early termination of supervised release under paragraph (1)(A) does not require extraordinary conduct or unforeseen circumstances. (8) Applicability The ability to seek the early termination of supervised release under paragraph (1)(A) shall not be affected by the plea agreement of the defendant. ;\n**(4)**\nin subsection (g)\u2014\n**(A)**\nin the subsection heading, by striking possession of controlled substance or firearm or for refusal To comply with drug testing and inserting distribution of a controlled substance or possession of a firearm ;\n**(B)**\nby amending paragraph (1) to read as follows:\n(1) (A) possesses a controlled substance with the intent to distribute; or (B) possesses a controlled substance, the possession of which may be punished under Federal law by imprisonment for a term exceeding 1 year; ;\n**(C)**\nin paragraph (2), by inserting or at the end;\n**(D)**\nby amending paragraph (3) to read as follows:\n(3) willfully refuses to comply with drug testing imposed as a condition of supervised release; ;\n**(E)**\nby striking paragraph (4); and\n**(F)**\nin the matter following paragraph (4), by striking subsection (e)(3) and inserting subsection (e)(1)(C) ; and\n**(5)**\nin subsection (k), in the second sentence, by striking subsection (e)(3) and inserting subsection (e)(1)(C) .\n#### 4. Law enforcement availability pay for probation and pretrial services officers\nNot later than 180 days after the date of enactment of this Act, the Director of the Administrative Office of the United States Courts, in consultation with the Director of the Office of Personnel Management, shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report containing a legislative proposal, and considerations for implementation of the proposal, that would provide law enforcement availability pay to Federal probation officers and pretrial services officers that is equal to that provided to criminal investigators under section 5545a of title 5, United States Code.\n#### 5. Allowing prisoners not sentenced to supervised release to apply earned time credits\nSection 3624(g) of title 18, United States Code, is amended\u2014\n**(1)**\nin the subsection heading, by striking Supervised ;\n**(2)**\nin paragraph (1)(D)\u2014\n**(A)**\nin clause (i), by striking supervised each place it appears; and\n**(B)**\nin clause (ii), by striking placed in supervised release and inserting released ;\n**(3)**\nin paragraph (3)\u2014\n**(A)**\nby striking (3) Supervised release .\u2014If the sentencing court and inserting the following:\n(3) Release (A) Supervised release imposed If the sentencing court ; and\n**(B)**\nby adding at the end the following:\n(B) Supervised release not imposed If the sentencing court did not impose a term of supervised release, the Director of the Bureau of Prisons may release the prisoner at an earlier date, not to exceed 12 months, based on the application of time credits under section 3632. ;\n**(4)**\nin paragraph (6)(A), by striking supervised ; and\n**(5)**\nin paragraph (7)(B), by striking supervised .\n#### 6. GAO report\n##### (a) Initiation of study\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall initiate a study on Federal post-release supervision and reentry services.\n##### (b) Report\nThe Comptroller General of the United States shall submit to Congress a report regarding the study under subsection (a), which shall include findings and potential recommendations related to\u2014\n**(1)**\nthe number of individuals that have been placed on Federal probation or supervised release since 2019;\n**(2)**\nthe process for transitioning an individual from the custody of the Bureau of Prisons to the Office of Probation and Pretrial Services or the custody of the United States Marshals Service;\n**(3)**\na review of Federal programs or funding sources that aim to assist individuals from the custody of the Bureau of Prisons with reentry, including\u2014\n**(A)**\nongoing mental health and substance use counseling, housing, medical care, education, and job placement; and\n**(B)**\nany changes in such programs or funding since 2019;\n**(4)**\na workforce assessment of judicial districts, including an analysis of\u2014\n**(A)**\nduring the most recent 2 years for which data is available, the number of officers, officer caseloads, and overtime hours worked, reported, or accrued; and\n**(B)**\nthe system for tracking overtime hours worked by officers of the Office of Probation and Pretrial Services; and\n**(5)**\nthe funding formula for probation offices, including an assessment of how that formula affects incentives for the recommendation of early termination of supervised release.",
      "versionDate": "2025-10-30",
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
        "actionDate": "2025-10-31",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5883",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Safer Supervision Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-11-25T16:52:43Z"
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
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3077is.xml"
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
      "title": "Safer Supervision Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safer Supervision Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T03:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to provide appropriate standards for the inclusion of a term of supervised release after imprisonment, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T03:48:19Z"
    }
  ]
}
```
