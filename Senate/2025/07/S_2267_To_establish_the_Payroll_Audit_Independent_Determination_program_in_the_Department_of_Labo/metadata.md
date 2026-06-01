# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2267?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2267
- Title: Ensuring Workers Get PAID Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2267
- Origin chamber: Senate
- Introduced date: 2025-07-14
- Update date: 2026-03-05T16:18:20Z
- Update date including text: 2026-03-05T16:18:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-14: Introduced in Senate
- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-14: Introduced in Senate

## Actions

- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2267",
    "number": "2267",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Ensuring Workers Get PAID Act of 2025",
    "type": "S",
    "updateDate": "2026-03-05T16:18:20Z",
    "updateDateIncludingText": "2026-03-05T16:18:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-14",
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
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T20:43:50Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "TN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2267is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2267\nIN THE SENATE OF THE UNITED STATES\nJuly 14, 2025 Mr. Sheehy (for himself, Mrs. Blackburn , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish the Payroll Audit Independent Determination program in the Department of Labor.\n#### 1. Short title\nThis Act may be cited as the Ensuring Workers Get PAID Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 2018, the Department of Labor launched the nationwide Payroll Audit Independent Determination pilot program (referred to in this section as PAID pilot program ).\n**(2)**\nThe Secretary of Labor, acting through the Administrator of the Wage and Hour Division, established the PAID pilot program to complement enforcement and compliance assistance tools undertaken by the Wage and Hour Division of the Department of Labor.\n**(3)**\nThe Secretary has a longstanding practice of providing self-audit and office audit programs, as noted by Secretary Marty Walsh in a response for the record following a hearing before the Committee on Education and Labor of the House of Representatives on June 9, 2021.\n**(4)**\nThe Wage and Hour Division, through the PAID pilot program, worked with employers on a voluntary basis to remedy unintentional violations of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ), which is the Federal statute establishing minimum wage, overtime pay, recordkeeping, and youth-employment requirements affecting employees in the private sector and in Federal, State, and local governments.\n**(5)**\nThe PAID pilot program yielded positive results for employers and employees. Between April 1, 2018, and September 15, 2019, the Wage and Hour Division concluded 74 PAID pilot program cases, representing less than one percent of all compliance actions under the Fair Labor Standards Act of 1938, with a total of $4,131,238 in back wages paid to 7,429 employees through such PAID pilot program cases.\n**(6)**\nSelf-audits through the PAID pilot program by employers returned more back wages to employees in less time than compliance actions overall. In fact, during the period described in paragraph (5)\u2014\n**(A)**\nthe average back wages paid per case for PAID pilot program cases ($55,828) were more than 4 times the average back wages paid per compliance action ($11,355);\n**(B)**\nthe average back wages paid per enforcement hour for PAID pilot program cases ($2,864) was more than 10 times greater than the average back wages paid per enforcement hour for compliance actions ($279);\n**(C)**\non average, nearly 10 times more employees received back wages in each PAID pilot program case than in investigations conducted using traditional methods;\n**(D)**\nself-audits through the PAID pilot program averaged 19 hours per case as compared to 41 hours per case for the Secretary conducted using traditional methods; and\n**(E)**\nself-audits through the PAID pilot program reached employers that the Wage and Hour Division would not typically prioritize for enforcement, including government establishments and industry sectors with higher wage occupations.\n#### 3. Definitions\nIn this Act:\n**(1) Affected employee**\nThe term affected employee means an employee affected by a violation of a minimum wage or overtime hours requirement of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ), excluding any employee subject to prevailing wage requirements under the H\u20131B, H\u20132B, or H\u20132A visa programs, subchapter IV of chapter 31 of title 40, United States Code (commonly referred to as the Davis-Bacon Act ), or chapter 67 of title 41, United States Code (commonly known as the Service Contract Act ).\n**(2) Administrator**\nThe term Administrator means the Administrator of the Wage and Hour Division of the Department of Labor.\n**(3) Employee**\nThe term employee \u2014\n**(A)**\nhas the meaning given such term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ); and\n**(B)**\nwith respect to an employer, includes a former employee of such employer.\n**(4) Employer**\nThe term employer has the meaning given such term in section 3 of such Act.\n**(5) Good faith**\nThe term good faith means, with respect to an employer applying for participation in the Payroll Audit Independent Determination program established under section 4, that such employer is not, at the time such employer submits an application for such program\u2014\n**(A)**\nunder investigation by the Secretary for an alleged violation of a minimum wage or overtime hours requirement of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ); or\n**(B)**\nsubject to a lawsuit related to an alleged violation of such a requirement.\n**(6) Secretary**\nThe term Secretary means the Secretary of Labor.\n**(7) Self-audit**\nThe term self-audit means an audit conducted by an employer to resolve inaccuracies by the employer in the computation of wages and overtime compensation required under the Fair Labor Standards Act of 1938 within the statute of limitations described in section 6(a) of the Portal-to-Portal Act of 1947 ( 29 U.S.C. 255(a) ).\n#### 4. Payroll Audit Independent Determination program\n##### (a) Program establishment\nThe Administrator shall establish a Payroll Audit Independent Determination program (referred to in this section as the program ) to foster collaboration with employers that inadvertently violate the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) to voluntarily remedy, within the statute of limitations described in section 6(a) of the Portal-to-Portal Act of 1947 ( 29 U.S.C. 255(a) ), unpaid minimum wages or overtime compensation owed to any affected employee under the Fair Labor Standards Act of 1938.\n##### (b) Application requirements\n**(1) Resources for compliance assistance**\nNot later than 30 days after the date of enactment of this Act, the Administrator shall make available to employers resources for assistance in complying with the Fair Labor Standards Act of 1938, including content regarding wage and hour requirements, which shall be offered online, through printed materials, and through other outreach activities.\n**(2) Application**\nAn employer seeking to participate in the program shall submit an application to the Administrator that includes\u2014\n**(A)**\nmaterials related to and the results of a self-audit, including\u2014\n**(i)**\nan identification of any practice of such employer identified in a self-audit that may violate a minimum wage or overtime compensation requirement of the Fair Labor Standards Act of 1938; and\n**(ii)**\na list of each employee who may be an affected employee with respect to such violation, including\u2014\n**(I)**\nthe period of time such employee would have been affected by such violation;\n**(II)**\npayroll records related to such employee for such period with information on the hours of work performed by such employee;\n**(III)**\ncalculations of unpaid minimum wages or overtime compensation owed to such employee under the Fair Labor Standards Act of 1938 with a description of the methodology of such calculation and supporting evidence; and\n**(IV)**\ncontact information for such employee;\n**(B)**\nan explanation of the scope of potential violations of a minimum wage or overtime compensation requirement of such Act for inclusion in a release of claims under subsection (d);\n**(C)**\nan assurance that any practice of such employer that violates a minimum wage or overtime compensation requirement of the Fair Labor Standards Act of 1938 that is identified in the self-audit has been corrected to comply with such Act;\n**(D)**\nan assurance that such employer has, prior to submitting such application, reviewed the compliance assistance resources made available under paragraph (1) and all program information, terms, and requirements;\n**(E)**\nan assurance that, on the date of submission of such application, such employer\u2014\n**(i)**\nis not involved in any litigation regarding any practice of such employer that is identified in the self-audit; and\n**(ii)**\nhas not received any communications from an employee or a representative of an employee seeking to litigate or settle claims related to any such practice; and\n**(F)**\nan assurance that no employee listed in subparagraph (A)(ii) is subject to a prevailing wage requirement under the H\u20131B, H\u20132B, or H\u20132A visa programs, subchapter IV of chapter 31 of title 40, United States Code (commonly referred to as the Davis-Bacon Act ), or chapter 67 of title 41, United States Code (commonly known as the Service Contract Act ).\n##### (c) Application review and approval\n**(1) Review and amendment**\nThe Administrator shall review each application submitted by an employer under subsection (b)(2). As part of such review, the Administrator shall\u2014\n**(A)**\nas necessary, consult with such employer regarding\u2014\n**(i)**\nthe self-audit and supporting materials submitted in the application; and\n**(ii)**\nthe process for approval of such application and settlement of unpaid minimum wages or overtime compensation owed to any affected employee under the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. );\n**(B)**\ninform such employer in a timely manner and prior to a determination on the approval of the application if additional information is needed to assess the unpaid minimum wages or overtime compensation owed to any affected employee for the violations of such Act identified in the application through the self-audit; and\n**(C)**\nprovide such employer an opportunity to amend such application to revise the scope of the practices of such employer that violate a minimum wage or overtime compensation requirement of the Fair Labor Standards Act of 1938 that are identified in the application through self-audit, to update the list of affected employees with respect to the practices at issue in the self-audit, and to update the calculations of unpaid minimum wages or overtime compensation owed to any affected employee as a result of such violations.\n**(2) Approval**\n**(A) In general**\nIf the conditions under subparagraph (B) are satisfied with respect to an application submitted under subsection (b)(2), the Administrator shall\u2014\n**(i)**\napprove the application\u2014\n**(I)**\nin the case the application has not been amended under paragraph (1)(C), not later than 30 days after such submission; or\n**(II)**\nin the case the application has been amended under paragraph (1)(C), not later than 30 days after the date of submission of such amended application; and\n**(ii)**\nsupervise the settlement under subsection (d), including the payment of any unpaid minimum wages or overtime compensation under the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) required through such settlement.\n**(B) Conditions for approval**\nAn application submitted under subsection (b)(2) shall be approved under subparagraph (A) if\u2014\n**(i)**\nwithin the scope of the violations identified by the employer through the application or an amendment to the application under paragraph (1)(C), the Administrator verifies that the self-audit and calculation of unpaid minimum wages or overtime compensation owed to any affected employee under the Fair Labor Standards Act of 1938 submitted in such application or amendment are accurate; and\n**(ii)**\nthe employer submitting the application\u2014\n**(I)**\nis determined to be acting in good faith regarding violations of the Fair Labor Standards Act of 1938 identified in such application or amendment;\n**(II)**\nhas not been found by the Administrator or any court of law to have violated a minimum wage or overtime compensation requirement of such Act during the 5 years immediately preceding submission of such application; and\n**(III)**\nhas not been approved for participation in the program prior to the submission of such application, unless\u2014\n**(aa)**\nsuch participation was for a distinct violation of the Fair Labor Standards Act of 1938 that the practice identified in the self-audit under subsection (b)(2); and\n**(bb)**\nsuch employer has submitted the necessary materials for the Administrator to verify that such employer is not engaging in the practice addressed by the previous participation of the employer in the program.\n##### (d) Settlement\n**(1) In general**\nFor each employer that submits an application under subsection (b)(2) that is approved under subsection (c)(2), the Administrator shall\u2014\n**(A)**\nprovide to the employer a description of the scope of the potential release of claims for violations of minimum wage or overtime compensation requirements of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) and a summary of any unpaid minimum wages or overtime compensation owed to each affected employee under such Act for such violations; and\n**(B)**\nissue a release form to each affected employee of such employer that describes the settlement terms, which shall include a written explanation of\u2014\n**(i)**\nthe waiver under paragraph (2)(B); and\n**(ii)**\nthe right of the affected employee receiving the offer for settlement to decline the offer for settlement and preserve any private right of action of the employee to recover any unpaid minimum wages or overtime compensation owed to the employee under the Fair Labor Standards Act of 1938 as a result of such violations.\n**(2) Acceptance of settlement**\n**(A) In general**\nAn affected employee offered a settlement through a release form under paragraph (1)(B) may accept or decline the offer.\n**(B) Waiver of private right of action**\nThe acceptance by an affected employee of an offer of settlement under subparagraph (A) shall, upon payment in full of any amounts owed to the employee under the settlement, constitute a waiver by such employee of any right such employee may have under section 16 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216 ) to a private right of action to recover unpaid minimum wages or overtime compensation, including any liquidated damages, for the violations addressed by the settlement.\n**(3) Payment of settlement**\nFor each affected employee that accepts a settlement through a release form under paragraph (1)(B), the employer shall\u2014\n**(A)**\npay such employee the full amount of unpaid minimum wages or overtime compensation owed to such employee under the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) for the violations addressed in the settlement; and\n**(B)**\nsubmit proof of payment of such full amount to the Administrator.\n##### (e) Additional requirements\n**(1) Denials**\nIn the case of an application submitted by an employer under subsection (b)(2) and not approved under subsection (c)(2), the Administrator may not\u2014\n**(A)**\nuse information submitted in the application in an investigation against the employer;\n**(B)**\nuse the fact such employer applied to the program as a basis for any future investigation, except in a case in which the Administrator has reason to believe that the health and safety of an employee is at risk due to an alleged violation related to a requirement enforced by the Secretary involving child labor, agricultural worker protections, or housing or transportation requirements under the H\u20132A or H\u20132B visa programs; or\n**(C)**\ncommunicate to any affected employee of such employer in response to receipt of such application to notify such employee of the private right of action of such employee to resolve potential violations of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ), particularly with respect to the wage practices at issue in the self-audit.\n**(2) Expansion of scope**\nThe Administrator may not expand the scope of the violations to be investigated or settled through an employer\u2019s participation in the program beyond the violations identified by the employer in the application submitted by the employer under subsection (b)(2) or the amended application submitted by the employer under subsection (c)(1)(C).\n**(3) No payments required**\nThe Administrator may not require any form of payment by an employer to apply, qualify, or participate in the program.\n**(4) Exemption from discovery**\nAny information submitted in an application to the program under subsection (b)(2), or an amendment to such application under subsection (c)(1)(C), may not be subject to discovery in a Federal or State court proceeding without the consent of the employer that submitted the application.\n##### (f) Retaliation\nSection 15(a)(3) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 215(a)(3) ) is amended by inserting before the semicolon the following: , or has accepted or declined to accept an offer for settlement under section 4(d) of the Ensuring Workers Get PAID Act of 2025 .",
      "versionDate": "2025-07-14",
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
        "actionDate": "2026-03-03",
        "text": "Placed on the Union Calendar, Calendar No. 464."
      },
      "number": "2299",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ensuring Workers Get PAID Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2025-12-04T19:08:03Z"
          },
          {
            "name": "Administrative remedies",
            "updateDate": "2025-12-04T19:08:03Z"
          },
          {
            "name": "Department of Labor",
            "updateDate": "2025-12-04T19:08:03Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-12-04T19:08:03Z"
          },
          {
            "name": "Labor standards",
            "updateDate": "2025-12-04T19:08:03Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2025-12-04T19:08:03Z"
          },
          {
            "name": "Personnel records",
            "updateDate": "2025-12-04T19:08:03Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2025-12-04T19:08:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-09-04T15:50:43Z"
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
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2267is.xml"
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
      "title": "Ensuring Workers Get PAID Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-26T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Workers Get PAID Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-26T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Payroll Audit Independent Determination program in the Department of Labor.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-26T03:18:20Z"
    }
  ]
}
```
