# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1355?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1355
- Title: REPAIR Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1355
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2025-05-19T14:08:54Z
- Update date including text: 2025-05-19T14:08:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1355",
    "number": "1355",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
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
    "title": "REPAIR Act of 2025",
    "type": "S",
    "updateDate": "2025-05-19T14:08:54Z",
    "updateDateIncludingText": "2025-05-19T14:08:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T21:45:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "ID"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1355is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1355\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Cassidy (for himself, Mr. Risch , and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo prescribe judicial review requirements for certain projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Revising and Enhancing Project Authorizations Impacted by Review Act of 2025 or the REPAIR Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given the term in section 551 of title 5, United States Code.\n**(2) Agency of jurisdiction**\nThe term agency of jurisdiction means any agency that is responsible for approving an authorization under authorizing legislation.\n**(3) Authorization**\nThe term authorization means any license, permit, authorization, approval, variance, consultation, finding, or other administrative decision (or any extension to or of any license, permit, authorization, approval, variance, consultation, finding, or other administrative decision) that is required or authorized under Federal law (including regulations) to design, plan, site, construct, reconstruct, commence operations of, modify, or operate a project.\n**(4) Authorizing legislation**\nThe term authorizing legislation means any of\u2014\n**(A)**\nthe Clean Air Act ( 42 U.S.C. 7401 et seq. );\n**(B)**\nthe Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. );\n**(C)**\nthe Natural Gas Act ( 15 U.S.C. 717 et seq. );\n**(D)**\nthe Federal Power Act ( 16 U.S.C. 791a et seq. );\n**(E)**\ndivision A of subtitle III of title 54, United States Code (formerly known as the National Historic Preservation Act ( 16 U.S.C. 470 et seq. ));\n**(F)**\nthe Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. );\n**(G)**\nthe Migratory Bird Treaty Act ( 16 U.S.C. 703 et seq. );\n**(H)**\nthe Act of June 8, 1940 ( 16 U.S.C. 668 et seq. ) (commonly known as the Bald and Golden Eagle Protection Act );\n**(I)**\nthe Marine Mammal Protection Act of 1972 ( 16 U.S.C. 1361 et seq. );\n**(J)**\nthe Coastal Zone Management Act of 1972 ( 16 U.S.C. 1451 et seq. );\n**(K)**\nthe Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 et seq. );\n**(L)**\nthe Mineral Leasing Act ( 30 U.S.C. 181 et seq. );\n**(M)**\nthe Safe Drinking Water Act ( 42 U.S.C. 300f et seq. ), as it relates to any State seeking to obtain primary enforcement authority for\u2014\n**(i)**\nthat Act pursuant to section 1413 of that Act ( 42 U.S.C. 300g\u20132 ); or\n**(ii)**\nan underground injection control program pursuant to section 1422 of that Act ( 42 U.S.C. 300h\u20131 );\n**(N)**\nthe Deepwater Port Act of 1974 ( 33 U.S.C. 1501 et seq. );\n**(O)**\nthe Atomic Energy Act of 1954 ( 42 U.S.C. 2011 et seq. );\n**(P)**\nthe Geothermal Steam Act of 1970 ( 30 U.S.C. 1001 et seq. );\n**(Q)**\nthe National Forest Management Act of 1976 ( Public Law 94\u2013588 ; 90 Stat. 2949);\n**(R)**\nthe Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1600 et seq. );\n**(S)**\nthe Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. );\n**(T)**\nthe Solid Waste Disposal Act ( 42 U.S.C. 6901 et seq. );\n**(U)**\nthe Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9601 et seq. );\n**(V)**\nchapter 2005 of title 54, United States Code (formerly known as the Urban Park and Recreation Recovery Act of 1978 ( 16 U.S.C. 2501 et seq. )); and\n**(W)**\nany other Federal law requiring an environmental review pursuant to the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).\n**(5) Council**\nThe term Council means the Federal Permitting Improvement Steering Council established by section 41002(a) of the FAST Act ( 42 U.S.C. 4370m\u20131(a) ).\n**(6) Direct and tangible harm**\nThe term direct and tangible harm means a harm with a causal connection to a project that causes\u2014\n**(A)**\nphysical illness or bodily injury; or\n**(B)**\nuncompensated economic loss.\n**(7) Environmental review**\nThe term environmental review means an assessment of environmental impact, prepared pursuant to the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), leading to the preparation of\u2014\n**(A)**\nan environmental assessment;\n**(B)**\na finding of no significant impact;\n**(C)**\nan environmental impact statement;\n**(D)**\na record of decision; or\n**(E)**\nany other review prepared to fulfill the requirements of that Act.\n**(8) Project**\nThe term project means an activity required to receive an authorization under authorizing legislation.\n**(9) Project sponsor**\nThe term project sponsor means the agency or other entity, including any private or public-private entity, that seeks approval from the agency of jurisdiction for a project.\n#### 3. Judicial review\n##### (a) Statute of limitations\n**(1) Definitions**\nIn this subsection:\n**(A) Initial authorization**\n**(i) In general**\nThe term initial authorization means an authorization issued by an agency of jurisdiction for a project following a request for the authorization from a project sponsor.\n**(ii) Exclusion**\nThe term initial authorization does not include any authorization issued by an agency of jurisdiction following an alteration made by a project sponsor pursuant to a mediation process described in subsection (d).\n**(B) Initial claim**\nThe term initial claim means a claim described in paragraph (2)(A).\n**(2) Claiming relating to initial authorizations**\n**(A) Initial claims**\nNotwithstanding any other provision of law, a claim seeking judicial review of any portion of the initial authorization process carried out for a project pursuant to authorizing legislation or an initial authorization issued by an agency of jurisdiction for a project shall be filed by the date that is 120 days after the date on which the final agency action with respect to the project has been taken, unless a shorter time is specified in the Federal law pursuant to which judicial review is sought.\n**(B) Subsequent action**\n**(i) In general**\nAny additional action relating to an initial claim, including an action seeking a preliminary injunction based on the initial claim, shall be filed not later than 120 days after the date on which the initial claim was filed.\n**(ii) Failure to submit subsequent claim**\nAn individual that fails to submit an additional action described in clause (i) relating to the filed initial claim by the deadline described in that clause shall\u2014\n**(I)**\ninvalidate the initial claim;\n**(II)**\nbe barred from bringing that additional claim; and\n**(III)**\nremove any such right of action relating to that initial claim.\n**(3) Other claims**\nAny other claim relating to the issuance of an authorization by an agency of jurisdiction for a project shall be subject to subsection (d).\n##### (b) Default remedy\n**(1) In general**\nIf a court of law determines that an agency did not comply with the requirements of authorizing legislation when granting an authorization for a project, the default remedy shall be to remand that authorization to the applicable agency.\n**(2) Limitation**\nA court of law shall not vacate, enjoin, or otherwise limit an authorization granted for a project unless the issuance of the authorization would present an imminent and substantial danger to human health or the environment for which there is no other equitable remedy available under law.\n##### (c) Right of action\nNotwithstanding any other provision of law, an individual seeking to bring a claim for judicial review of the approval of an authorization for a project may only bring the claim if the individual will suffer a direct and tangible harm because of the authorization for which the individual is seeking judicial review if the harm was not analyzed in the approval of the initial authorization (as defined in subsection (a)(1)).\n##### (d) Right of alteration\n**(1) In general**\nIf an authorization for a project is enjoined, remanded, or vacated by a court of law, the project sponsor and the agency of jurisdiction shall participate in a mediation process overseen by the Council\u2014\n**(A)**\nto address the reasons for the injunction, remand, or vacatur; and\n**(B)**\nto reauthorize the project for development.\n**(2) Process**\n**(A) Remediation proposals**\nSubject to subparagraph (B)(i), not later than 60 days after the date on which an authorization for a project is enjoined, remanded, or vacated by a court of law, the project sponsor and the agency of jurisdiction shall each submit to the Council remediation proposals\u2014\n**(i)**\nto address any identified issues that can be fully resolved; or\n**(ii)**\nto attempt to mitigate the identified issues if the issues cannot be fully resolved.\n**(B) Extension**\n**(i) In general**\nA project sponsor may request from the Council an extension of not more than 120 days to complete a remediation proposal described in subparagraph (A).\n**(ii) Approval required**\nIf the Council receives a request from a project sponsor for an extension under clause (i), the Council shall approve that request.\n**(iii) Treatment of the agency of jurisdiction**\nIf an extension is requested and approved under clauses (i) and (ii), respectively, an agency of jurisdiction may, notwithstanding subparagraph (A), submit the remediation proposal required under that subparagraph (A) within the extension period described in clause (i).\n**(C) Agency compliance**\nIf an agency of jurisdiction fails to submit a remediation proposal in the time period described in subparagraph (A) or (B)(i), as applicable, the Council shall\u2014\n**(i)**\napprove the remediation proposal submitted by the project sponsor; and\n**(ii)**\ndirect the agency of jurisdiction to reauthorize all applicable authorizations for the project.\n**(D) Council review**\n**(i) In general**\nNot later than 60 days after the date on which a project sponsor and an agency of jurisdiction submit a remediation proposal in accordance with subparagraph (A) or (B)(i), as applicable, the Council shall\u2014\n**(I)**\nhold any necessary joint meetings between the project sponsor and the agency of jurisdiction to assist in reaching a final remediation plan described in clause (ii);\n**(II)**\ncomplete a final remediation plan; and\n**(III)**\ndirect the agency of jurisdiction to reauthorize the project based on that final remediation plan.\n**(ii) Final remediation plan**\n**(I) In general**\nA final remediation plan described in clause (i) shall contain any alterations to a project necessary to address the reasons for which a court of law enjoined, remanded, vacated, or otherwise limited an authorization for the applicable project.\n**(II) Form**\nA final remediation plan described in clause (i) shall\u2014\n**(aa)**\naccept the remediation proposal of the project sponsor; or\n**(bb)**\nalter the remediation proposal of the project sponsor based on the remediation proposal of the agency of jurisdiction.\n**(III) Alterations**\nTo the maximum extent practicable, alterations described in subclause (II)(bb) shall represent an intermediate position between the remediation proposal of the project sponsor and the remediation proposal of the agency of jurisdiction.\n**(IV) Length of final remediation plan**\nThe text of a final remediation plan shall not exceed 50 pages.\n**(iii) Right of acceptance**\n**(I) In general**\nAt any point in the 60-day period described in clause (i), a project sponsor or an agency of jurisdiction may submit to the Council in writing an acceptance of the remediation proposal of the other party.\n**(II) Reauthorization**\nIf the Council receives an acceptance under subclause (I), the Council shall\u2014\n**(aa)**\nconsider the accepted remediation proposal to be the final remediation plan; and\n**(bb)**\ndirect the agency of jurisdiction to reauthorize all authorizations for the project.\n**(iv) Meetings**\nThe Council shall hold not less than 1 meeting between a project sponsor and an agency of jurisdiction to address any necessary areas of dispute between the applicable remediation plans.\n**(v) Completion**\nOn completion of a final remediation plan under clause (ii), the Council shall\u2014\n**(I)**\nmake public the final remediation plan in a manner consistent with the authorization approval process of the agency of jurisdiction; and\n**(II)**\ndirect the agency of jurisdiction to reauthorize all authorizations for the project.\n**(vi) Compliance**\nIf the Council fails to direct the agency of jurisdiction to reauthorize all authorizations for the project within the 60-day period described in clause (i), the agency of jurisdiction shall\u2014\n**(I)**\nconsider the remediation proposal of the project sponsor to be the final remediation plan; and\n**(II)**\nreauthorize all authorizations for the project in accordance with the final remediation plan.\n**(E) Additional meetings**\nAt the request of a project sponsor, following the date on which an authorization for a project is enjoined, remanded, or vacated by a court of law, but before the date on which a project sponsor and an agency of jurisdiction submit a remediation proposal under subparagraph (A) or (B)(i), as applicable, the Council may hold meetings between the agency of jurisdiction and the project sponsor in an attempt to align the parties on remediation proposals.\n**(F) Treatment of additional analyses**\n**(i) In general**\nTo the maximum extent practicable, and except as provided in clause (ii), all remediation proposals and final remediation plans described in subparagraph (D)(ii) shall only use existing information, data, and analyses used in the initial authorization (as defined in subsection (a)(1)) or presented as a part of the initial claim (as defined in that subsection) and subsequent judicial process.\n**(ii) Additional analyses**\nIf additional analysis is required to fulfill a court order, all final remediation plans described in subparagraph (D)(ii) shall\u2014\n**(I)**\ndesignate a singular agency of jurisdiction to perform the analysis;\n**(II)**\nallow for not more than 90 days to perform the analysis;\n**(III)**\ndesignate the court order as fulfilled and the project authorization re-approved if the designated agency does not complete the analysis in the 90-day period described in subclause (II); and\n**(IV)**\nestablish clear actions to be taken in relation to the final remediation plan and the authorization dependent on the potential outcomes of the additional analysis.\n**(3) Right of additional review**\nA final remediation plan described in paragraph (2)(D)(ii) shall not be subject to judicial review or further right of action by an individual or entity other than the project sponsor.\n**(4) Reauthorization**\n**(A) In general**\nAn agency of jurisdiction shall reauthorize all authorizations for a project not later than 15 days after the date on which a final remediation plan described in paragraph (2)(D)(ii) is completed.\n**(B) Failure to reauthorize a project**\nIf an agency of jurisdiction fails to reauthorize a project and submit to the project sponsor any necessary authorization paperwork within the 15-day period described in subparagraph (A), the project sponsor may begin any necessary actions reliant on the authorization to complete the project.\n##### (e) Venue\nA claim seeking judicial review of an authorization issued by an agency of jurisdiction for a project shall be filed\u2014\n**(1)**\nin the court the jurisdiction of which contains the location of the project that the authorization applies to; or\n**(2)**\nif the location of the project transverses the jurisdiction of multiple courts, in the court the jurisdiction of which contains the location in which the largest financial investment will be made with respect to the project.\n##### (f) Random assignment of cases\nTo the maximum extent practicable, district courts of the United States and courts of appeals of the United States shall randomly assign cases seeking judicial review of any authorization issued by an agency of jurisdiction for a project to judges appointed, designated, or assigned to sit as judges of the court in a manner to avoid the appearance of favoritism or bias.\n##### (g) Publication of judicial review time periods\n**(1) In general**\nThe Council shall maintain a public database (referred to in this subsection as the database ) of any claim relating to the issuance of an authorization by an agency of jurisdiction that\u2014\n**(A)**\nis subject to judicial review; and\n**(B)**\nhas not been adjudicated within 90 days after the date on which the claim was assigned to a judge.\n**(2) Reporting requirements**\n**(A) In general**\nIn the case of a claim described in paragraph (1) that has not been adjudicated within 90 days after the date on which the claim is assigned to a judge, the Director of the Administrative Office of the United States Courts shall submit to the Council a report, which shall include\u2014\n**(i)**\nthe name of the claim;\n**(ii)**\nthe authorizing legislation pursuant to which the initial authorization (as defined in subsection (a)(1)) was issued;\n**(iii)**\nthe name of the plaintiff;\n**(iv)**\nthe name of the defendant;\n**(v)**\nthe date on which the claim was filed;\n**(vi)**\nthe name of the court; and\n**(vii)**\nthe name of the judge to which the claim was assigned.\n**(B) Alternate reporting methods**\n**(i) In general**\nA plaintiff or defendant involved in a claim may self-report the information described in clauses (i) through (vii) of subparagraph (A).\n**(ii) Publication**\nThe Council shall ensure that the availability to self-report as described in clause (i) is publicized\u2014\n**(I)**\non the home page of the website of the Council; and\n**(II)**\nin any other manner determined to be appropriate by the Council.\n**(iii) Notification to applicable court**\nFor each matter self-reported to the Council under clause (i), the Council shall notify the applicable court to confirm that the information described in clauses (i) through (vii) of subparagraph (A) received by the Council is accurate.\n**(3) Maintenance of judicial review timelines**\nWith respect to each claim in the database, the Council shall update the database not less frequently than daily to reflect the number of days the claim has been under judicial review.\n**(4) Publication**\nNot later than 5 business days after the date on which the Council receives a report from the Director of the Administrative Office of the United States Courts under subparagraph (A) of paragraph (2) or from a plaintiff or defendant under subparagraph (B) of that paragraph, as applicable, the Council shall update the database to include the information contained in the report.\n**(5) Council reporting**\n**(A) In general**\nNot less frequently than once per calendar year, the Council shall publish and submit to the committees described in subparagraph (D) a report containing\u2014\n**(i)**\na list of all cases with claims that were reported to the Council under paragraph (2);\n**(ii)**\na list of all courts with multiple cases with claims reported under paragraph (2), which shall be\u2014\n**(I)**\nlisted by name with the total number of applicable cases on file with each court\u2014\n**(aa)**\nin the year preceding the date on which the applicable report is submitted; and\n**(bb)**\nin total since the date of enactment of this Act; and\n**(II)**\nordered according to the largest number, from largest to smallest, of late cases per court in the year preceding the date on which the applicable report is submitted;\n**(iii)**\na list of all judges with multiple cases with claims reported under paragraph (2), which shall be\u2014\n**(I)**\nlisted by name with the total number of late cases assigned to each judge\u2014\n**(aa)**\nin the year preceding the date on which the applicable report is submitted; and\n**(bb)**\nin total since the date of enactment of this Act; and\n**(II)**\nordered according to the largest number, from largest to smallest, of late cases per judge since the date of enactment of this Act;\n**(iv)**\nthe name of any judge that has failed to report a claim in accordance with paragraph (2)(A); and\n**(v)**\nany other information that the Council determines to be necessary to ensure timely review of claims relating to the issuance of an authorization.\n**(B) More frequent reporting**\nThe Council may publish the report required under subparagraph (A) more frequently than once per calendar year, subject to the condition that the Council shall not publish the report more frequently than once per quarter.\n**(C) Publication**\nAny report prepared by the Council under subparagraph (A) shall be\u2014\n**(i)**\npublished in the Federal Register; and\n**(ii)**\nmade available on the website of the Council.\n**(D) Committees described**\nThe committees referred to in subparagraph (A) are\u2014\n**(i)**\nthe Committee on Environment and Public Works of the Senate;\n**(ii)**\nthe Committee on the Judiciary of the Senate;\n**(iii)**\nthe Committee on Energy and Natural Resources of the Senate;\n**(iv)**\nthe Committee on Natural Resources of the House of Representatives;\n**(v)**\nthe Committee on the Judiciary of the House of Representatives; and\n**(vi)**\nthe Committee on Energy and Commerce of the House of Representatives.\n##### (h) Treatment of existing authorization requests\nFor a project sponsor that has submitted a project to an agency of jurisdiction for approval of an authorization on or before the date of enactment of this Act, the judicial review requirements described in this section shall apply to any authorization granted for the project.\n##### (i) Treatment of existing judicial reviews\nFor any authorization subject to judicial review as of the date of enactment of this Act, the judicial review processes described in this section shall apply to such judicial review.\n##### (j) Savings provision\nNothing in this section\u2014\n**(1)**\nestablishes a right of action under any authorizing legislation relating to an environmental review that does not already provide for a right of action relating to that environmental review; or\n**(2)**\nprohibits any lawful action taken by a project sponsor that has been denied the ability\u2014\n**(A)**\nto appeal an initial rejection of a project by the agency of jurisdiction;\n**(B)**\nto appeal a rejection by the agency of jurisdiction relating to 1 or more attempts to address the issues identified as a result of a previous injunction, remand, or vacatur of an authorization decision; or\n**(C)**\nto resubmit a project in a manner that addresses the reasons for the rejection of that project by the agency of jurisdiction.\n#### 4. Judicial standing under NEPA\nTitle I of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4331 et seq. ) is amended by adding at the end the following:\n112. Judicial standing Nothing in this title, or any environmental review (as defined in section 2 of the REPAIR Act of 2025 ) carried out pursuant to this title, provides a judicial right of action under this title or subchapter II of chapter 5, and chapter 7, of title 5, United States Code (commonly known as the Administrative Procedure Act ), relating to the approval of an authorization (as defined in that section) for a project (as defined in that section) that uses an applicable environmental review (as so defined). .",
      "versionDate": "2025-04-08",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-05-19T14:08:54Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1355is.xml"
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
      "title": "REPAIR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T02:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REPAIR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T02:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Revising and Enhancing Project Authorizations Impacted by Review Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T02:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prescribe judicial review requirements for certain projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T02:33:18Z"
    }
  ]
}
```
