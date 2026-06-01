# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3394?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3394
- Title: SAFE Act
- Congress: 119
- Bill type: S
- Bill number: 3394
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3394",
    "number": "3394",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "SAFE Act",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
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
            "date": "2025-12-09T19:35:12Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-09T19:35:12Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "TN"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "SC"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NH"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NV"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-02",
      "state": "ME"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "AZ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "AZ"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MI"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3394is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3394\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Grassley (for himself, Mr. Durbin , Mrs. Blackburn , and Mr. Graham ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo direct the United States Sentencing Commission to amend the sentencing guideline relating to child sexual abuse material.\n#### 1. Short title\nThis Act may be cited as the Sentencing Accountability For Exploitation Act or the SAFE Act .\n#### 2. Amendment of Federal sentencing guideline relating to child sexual abuse material\n##### (a) Definitions\nIn this section:\n**(1) Child**\nThe term child means an individual who has not attained 18 years of age.\n**(2) Child sexual abuse material**\nThe term child sexual abuse material has the meaning given the term child pornography in section 2256(8) of title 18, United States Code.\n**(3) Prohibited sexual conduct against a child**\nThe term prohibited sexual conduct against a child \u2014\n**(A)**\nmeans\u2014\n**(i)**\nconduct committed against a child relating to\u2014\n**(I)**\nkidnapping;\n**(II)**\nillegal sexual abuse, contact, or activity;\n**(III)**\nlive streaming of child sexual abuse;\n**(IV)**\nusing a child to produce child sexual abuse material; or\n**(V)**\nsexual exploitation, including child sex trafficking; or\n**(ii)**\nan attempt or conspiracy to engage in any conduct described in subclauses (I) through (V) of clause (i);\n**(B)**\ndoes not include conduct involving or similar to advertising, transporting, mailing, distributing, receiving, possession, accessing, or viewing child sexual abuse material; and\n**(C)**\ndoes not require a conviction.\n##### (b) Directive\nPursuant to its authority under section 994(p) of title 28, United States Code, the United States Sentencing Commission shall review and amend the Federal sentencing guidelines and policy statements applicable to persons convicted of an offense under section 1466A, 2251(d)(1)(A), 2252, 2252A, or 2260(b) of title 18, United States Code, in order to reflect the intent of Congress that penalties for the offense under the guidelines and policy statements\u2014\n**(1)**\nappropriately account for\u2014\n**(A)**\nthe actual and potential harm to victims and to the public from the offense; and\n**(B)**\nchanges that have occurred since the relevant guidelines and policy statements were last amended with respect to\u2014\n**(i)**\ntypical offense behavior; and\n**(ii)**\nthe use of modern computer and internet technologies; and\n**(2)**\nto better reflect the current spectrum of offender culpability.\n##### (c) Requirements\nIn carrying out subsection (b), the United States Sentencing Commission shall\u2014\n**(1)**\nensure that the Federal sentencing guidelines and policy statements reflect\u2014\n**(A)**\nthe seriousness of the offenses described in that subsection;\n**(B)**\nthe need to afford adequate deterrence to commission of the offenses;\n**(C)**\nthe need for just punishment for the offenses;\n**(D)**\nthe need to protect the public from further crimes of a defendant convicted of any such offense; and\n**(E)**\nthe need to differentiate among offenders based on their culpability and potential dangerousness;\n**(2)**\navoid duplicative punishment within the applicable guidelines and under the Federal sentencing guidelines for substantially the same conduct;\n**(3)**\ndevelop a guideline that accounts for\u2014\n**(A)**\nwhether, prior to, during, or after the offense at issue, the defendant engaged in, conspired to engage in, or attempted to engage in\u2014\n**(i)**\nan act of prohibited conduct against a child; or\n**(ii)**\na pattern of activity involving prohibited conduct against a child, whether involving a single victim or multiple victims;\n**(B)**\nwhether, prior to, during, or after the offense at issue, the defendant\u2014\n**(i)**\nparticipated in a group dedicated to child sexual abuse material or prohibited conduct against a child; or\n**(ii)**\nencouraged, instructed, required, or similarly caused another individual to commit an offense involving child sexual abuse material or prohibited conduct against a child;\n**(C)**\nwhether the defendant engaged in multiple acts, not accounted for in the defendant\u2019s criminal history or counts of conviction, involving child sexual abuse material over an extended period of time or with a high degree of frequency;\n**(D)**\nwhether the defendant intentionally used, or promoted the use of, software, technology, procedures, or any other means to conceal the offense or the identity or location of the defendant or any victim, or to destroy evidence for an improper purpose, unless accounted for in the conduct of conviction;\n**(E)**\nwhether 3 or more online channels, technologies, platforms, or methods were used to commit the offense;\n**(F)**\ngradations in\u2014\n**(i)**\nthe severity of the depicted sexually explicit conduct, including especially severe physical or emotional trauma; and\n**(ii)**\nthe age or physical development of the minor;\n**(G)**\nthe number of items of child sexual abuse material or the number of victims involved in the offense;\n**(H)**\nwhether the offense involved distribution of child sexual abuse material, accounting for the nature of the distribution, including\u2014\n**(i)**\ndistribution in order to receive any valuable consideration; and\n**(ii)**\ndistribution through any method that does not limit who can obtain the material or how many individuals can obtain the material;\n**(I)**\nwhether the offense involved the production, creation, or manufacture of child sexual abuse material that is not subject to the cross reference in section 2G2.2(c)(1) of the United States Sentencing Guidelines Manual to section 2G2.1 of the Manual;\n**(J)**\nwhether the offense was the direct and proximate cause of the victim\u2019s death by suicide; and\n**(K)**\nany other conduct or factors that the United States Sentencing Commission determines appropriate to reflect the seriousness of the offense and differentiate among offenders;\n**(4)**\nmake any necessary conforming changes to the guidelines; and\n**(5)**\nensure that the guidelines adequately meet the purposes of sentencing, as set forth in section 3553(a)(2) of title 18, United States Code.\n##### (d) Authority for United States Sentencing Commission\nIn carrying out this section, the United States Sentencing Commission\u2014\n**(1)**\nmay amend provisions of the Federal sentencing guidelines that were promulgated pursuant to any other specific congressional directives or legislation directly amending the guidelines and promulgate amendments that would result in sentencing ranges different than those that would have applied under such directives or legislation; and\n**(2)**\nin developing a guideline that comports with the requirements of this section, particularly accounting for the factors set forth in subsection (c)(3)\u2014\n**(A)**\nmay\u2014\n**(i)**\ndesign the specific offense characteristics, including the increase in offense level that each offense characteristic would provide; and\n**(ii)**\ndefine any terms; and\n**(B)**\nmay not lower the applicable base offense level provided in section 2G2.2(a) of the United States Sentencing Guidelines Manual as in effect on the date of enactment of this Act.\n##### (e) Repeals\n**(1) Laws**\nThe following provisions of law are repealed:\n**(A)**\nSection 632 of the Treasury, Postal Service and General Government Appropriations Act, 1992 ( 28 U.S.C. 994 note; Public Law 102\u2013141 ).\n**(B)**\nSections 2 and 3 of the Sex Crimes Against Children Prevention Act of 1995 ( 28 U.S.C. 994 note; Public Law 104\u201371 ).\n**(C)**\nSection 401(i)(1) of the Prosecutorial Remedies and Other Tools to end the Exploitation of Children Today Act of 2003 ( 28 U.S.C. 994 note; Public Law 108\u201321 ).\n**(2) Guidelines**\nSection 2G2.2(b) of the United States Sentencing Commission Guidelines Manual is amended by striking paragraph (7).",
      "versionDate": "2025-12-09",
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
        "actionDate": "2026-03-02",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 346."
      },
      "number": "6719",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "James T. Woods Act",
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
        "updateDate": "2026-01-07T17:02:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-09",
    "originChamber": "Senate",
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
          "measure-id": "id119s3394",
          "measure-number": "3394",
          "measure-type": "s",
          "orig-publish-date": "2025-12-09",
          "originChamber": "SENATE",
          "update-date": "2026-03-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3394v00",
            "update-date": "2026-03-02"
          },
          "action-date": "2025-12-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Sentencing Accountability For Exploitation Act or the SAFE Act</strong></p><p>This bill directs the U.S. Sentencing Commission to review and amend its guidelines and policy statements applicable to federal criminal offenses involving the production, receipt, transport, shipment, or distribution of child sexual abuse material to (1) account for the actual and potential harm from the offense and changes since the last amendments with respect to the typical offense behavior and modern technologies, and (2) better reflect the spectrum of offender culpability.</p>"
        },
        "title": "SAFE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3394.xml",
    "summary": {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sentencing Accountability For Exploitation Act or the SAFE Act</strong></p><p>This bill directs the U.S. Sentencing Commission to review and amend its guidelines and policy statements applicable to federal criminal offenses involving the production, receipt, transport, shipment, or distribution of child sexual abuse material to (1) account for the actual and potential harm from the offense and changes since the last amendments with respect to the typical offense behavior and modern technologies, and (2) better reflect the spectrum of offender culpability.</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119s3394"
    },
    "title": "SAFE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sentencing Accountability For Exploitation Act or the SAFE Act</strong></p><p>This bill directs the U.S. Sentencing Commission to review and amend its guidelines and policy statements applicable to federal criminal offenses involving the production, receipt, transport, shipment, or distribution of child sexual abuse material to (1) account for the actual and potential harm from the offense and changes since the last amendments with respect to the typical offense behavior and modern technologies, and (2) better reflect the spectrum of offender culpability.</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119s3394"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3394is.xml"
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
      "title": "SAFE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sentencing Accountability For Exploitation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the United States Sentencing Commission to amend the sentencing guideline relating to child sexual abuse material.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:33:18Z"
    }
  ]
}
```
