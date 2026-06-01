# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/768?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/768
- Title: Invest to Protect Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 768
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-04-03T01:23:34Z
- Update date including text: 2026-04-03T01:23:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/768",
    "number": "768",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Invest to Protect Act of 2025",
    "type": "S",
    "updateDate": "2026-04-03T01:23:34Z",
    "updateDateIncludingText": "2026-04-03T01:23:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
            "date": "2025-02-27T16:46:39Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-27T16:46:39Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "LA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "DE"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "ME"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "AZ"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s768is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 768\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Ms. Cortez Masto (for herself, Mr. Grassley , Mr. Durbin , Mr. Blumenthal , Mr. Warnock , Mr. Cassidy , Mr. Coons , Ms. Collins , Mr. Kelly , Mr. Young , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a grant program to provide assistance to local law enforcement agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Invest to Protect Act of 2025 .\n#### 2. Grant program\n##### (a) Definitions\nIn this Act:\n**(1) De-escalation training**\nThe term de-escalation training means training relating to taking action or communicating verbally or non-verbally during a potential force encounter in an attempt to stabilize the situation and reduce the immediacy of the threat so that more time, options, and resources can be called upon to resolve the situation without the use of force or with a reduction in the force necessary.\n**(2) Director**\nThe term Director means the Director of the Office.\n**(3) Eligible local government**\nThe term eligible local government means\u2014\n**(A)**\na county, municipality, town, township, village, parish, borough, or other unit of general government below the State level that employs fewer than 175 law enforcement officers; and\n**(B)**\na Tribal government that employs fewer than 175 law enforcement officers.\n**(4) Law enforcement officer**\nThe term law enforcement officer has the meaning given the term career law enforcement officer in section 1709 of title I the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10389 ).\n**(5) Office**\nThe term Office means the Office of Community Oriented Policing Services of the Department of Justice.\n##### (b) Establishment\nThere is established within the Office a grant program to\u2014\n**(1)**\nprovide training and access to mental health resources to local law enforcement officers; and\n**(2)**\nimprove the recruitment and retention of local law enforcement officers.\n##### (c) Authority\nNot later than 120 days after the date of enactment of this Act, the Director shall award grants to eligible local governments as a part of the grant program established under subsection (b).\n##### (d) Applications\n**(1) Barriers**\nThe Attorney General shall determine what barriers exist to establishing a streamlined application process for grants under this section.\n**(2) Report**\n**(A) In general**\nNot later than 60 days after the date of enactment of this Act, the Attorney General shall submit to Congress a report that includes a plan to execute a streamlined application process for grants under this section under which an eligible local government seeking a grant under this section can reasonably complete the application in not more than 2 hours.\n**(B) Contents of plan**\nThe plan required under subparagraph (A) may include a plan for\u2014\n**(i)**\nproactively providing eligible local governments seeking a grant under this section with information on the data eligible local governments will need to prepare before beginning the grant application; and\n**(ii)**\nensuring technical assistance is available for eligible local governments seeking a grant under this section before and during the grant application process, including through dedicated liaisons within the Office.\n**(3) Applications**\nIn selecting eligible local governments to receive grants under this section, the Director shall use the streamlined application process described in paragraph (2)(A).\n##### (e) Eligible activities\nAn eligible local government that receives a grant under this section may use amounts from the grant only for\u2014\n**(1)**\nde-escalation training for law enforcement officers;\n**(2)**\nvictim-centered training for law enforcement officers in handling situations of domestic violence;\n**(3)**\nevidence-based law enforcement safety training for\u2014\n**(A)**\nactive shooter situations;\n**(B)**\nthe safe handling of illicit drugs and precursor chemicals;\n**(C)**\nrescue situations;\n**(D)**\nrecognizing and countering ambush attacks; or\n**(E)**\nresponse to calls for service involving\u2014\n**(i)**\npersons with mental health needs;\n**(ii)**\npersons with substance use disorders;\n**(iii)**\nveterans;\n**(iv)**\npersons with disabilities;\n**(v)**\nvulnerable youth;\n**(vi)**\npersons who are victims of domestic violence, sexual assault, or trafficking; or\n**(vii)**\npersons experiencing homelessness or living in poverty;\n**(4)**\nthe offsetting of overtime costs associated with scheduling issues relating to the participation of a law enforcement officer in the training described in paragraphs (1) through (3), (9), and (10);\n**(5)**\na signing bonus for a law enforcement officer in an amount determined by the eligible local government;\n**(6)**\na retention bonus for a law enforcement officer\u2014\n**(A)**\nin an amount determined by the eligible local government that does not exceed 20 percent of the salary of the law enforcement officer; and\n**(B)**\nwho\u2014\n**(i)**\nhas been employed at the law enforcement agency for not fewer than 5 years;\n**(ii)**\nhas not been found by an internal investigation to have engaged in serious misconduct; and\n**(iii)**\ncommits to remain employed by the law enforcement agency for not less than 3 years after the date of receipt of the bonus;\n**(7)**\na stipend for the graduate education of law enforcement officers in the area of mental health, public health, or social work, which shall not exceed the lesser of\u2014\n**(A)**\n$10,000; or\n**(B)**\nthe amount the law enforcement officer pays towards such graduate education;\n**(8)**\nproviding access to patient-centered behavioral health services for law enforcement officers, which may include resources for risk assessments, evidence-based, trauma-informed care to treat post-traumatic stress disorder or acute stress disorder, peer support and counselor services and family supports, and the promotion of improved access to high quality mental health care through telehealth;\n**(9)**\nthe implementation of evidence-based best practices and training on the use of lethal and nonlethal force;\n**(10)**\nthe implementation of evidence-based best practices and training on the duty of care and the duty to intervene; and\n**(11)**\ndata collection for police practices relating to officer and community safety.\n##### (f) Reporting requirements for grant recipients\n**(1) In general**\nThe Director shall establish reasonable reporting requirements specifically relating to a grant awarded under this section for eligible local governments that receive such a grant in order to assist with the evaluation by the Office of the program established under this section.\n**(2) Considerations**\nIn establishing requirements under paragraph (1), the Director shall consider the capacity of law enforcement agencies with fewer than 175 officers to collect and report information.\n##### (g) Disclosure of officer recruitment and retention bonuses\n**(1) In general**\nNot later than 60 days after the date on which an eligible local government that receives a grant under this section awards a signing or retention bonus described in paragraph (5) or (6) of subsection (e), the eligible local government shall disclose to the Director and make publicly available on a website of the eligible local government the amount of the bonus.\n**(2) Report**\nThe Attorney General shall submit to the appropriate congressional committees an annual report that includes each signing or retention bonus disclosed under paragraph (1) during the preceding year.\n##### (h) Grant accountability\n**(1) In general**\nAll grants awarded by the Director under this section shall be subject to the accountability provisions described in this subsection.\n**(2) Audit requirement**\n**(A) Definition**\nIn this paragraph, the term unresolved audit finding means a finding in the final audit report of the Inspector General of the Department of Justice that the audited grantee has used grant funds for an unauthorized expenditure or otherwise unallowable cost that is not closed or resolved within 12 months from the date when the final audit report is issued.\n**(B) Audits**\nBeginning in the first fiscal year beginning after the date of enactment of this subsection, and in each fiscal year thereafter, the Inspector General of the Department of Justice shall conduct audits of recipients of grants under this section to prevent waste, fraud, and abuse of funds by grantees. The Inspector General of the Department of Justice shall determine the appropriate number of grantees to be audited each year.\n**(C) Mandatory exclusion**\nA recipient of grant funds under this section that is found to have an unresolved audit finding shall not be eligible to receive grant funds under this section during the first 3 fiscal years beginning after the end of the 12-month period described in subparagraph (A).\n**(D) Reimbursement**\nIf an eligible local government is awarded grant funds under this section during the 3-fiscal-year period during which the eligible local government is barred from receiving grants under subparagraph (C), the Attorney General shall\u2014\n**(i)**\ndeposit an amount equal to the amount of the grant funds that were improperly awarded to the grantee into the General Fund of the Treasury; and\n**(ii)**\nseek to recoup the costs of the repayment to the fund from the grant recipient that was erroneously awarded grant funds.\n**(3) Annual certification**\nBeginning in the fiscal year during which audits commence under paragraph (2)(B), the Attorney General shall submit to the Committee on the Judiciary and the Committee on Appropriations of the Senate and the Committee on the Judiciary and the Committee on Appropriations of the House of Representatives an annual certification\u2014\n**(A)**\nindicating whether\u2014\n**(i)**\nall audits issued by the Office of the Inspector General of the Department of Justice under paragraph (2) have been completed and reviewed by the appropriate Assistant Attorney General or Director;\n**(ii)**\nall mandatory exclusions required under paragraph (2)(C) have been issued; and\n**(iii)**\nall reimbursements required under paragraph (2)(D) have been made; and\n**(B)**\nthat includes a list of any grant recipients excluded under paragraph (2) from the previous year.\n##### (i) Program evaluation\nNot less frequently than annually, the Attorney General shall analyze the information provided by eligible local governments pursuant to the reporting requirements established under subsection (f)(1) to evaluate the efficacy of programs funded by the grant program under this section.\n##### (j) Preventing duplicative grants\n**(1) In general**\nBefore the Director awards a grant to an eligible local government under this section, the Attorney General shall compare potential grant awards with other grants awarded by the Attorney General to determine if grant awards are or have been awarded for a similar purpose.\n**(2) Report**\nIf the Attorney General awards grants to the same applicant for a similar purpose, whether through the grant program under this section or another grant program administered by the Department of Justice, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that includes\u2014\n**(A)**\na list of all such grants awarded, including the total dollar amount of any such grants awarded; and\n**(B)**\nthe reason the Attorney General awarded multiple grants to the same applicant for a similar purpose.\n##### (k) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section not more than $50,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-04-08",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2711",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Invest to Protect Act of 2025",
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
        "updateDate": "2025-03-21T16:01:52Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s768is.xml"
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
      "title": "Invest to Protect Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Invest to Protect Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a grant program to provide assistance to local law enforcement agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:22Z"
    }
  ]
}
```
