# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3959?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3959
- Title: Smarter Sentencing Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3959
- Origin chamber: Senate
- Introduced date: 2026-03-02
- Update date: 2026-05-28T19:20:52Z
- Update date including text: 2026-05-28T19:20:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-02: Introduced in Senate
- 2026-03-02 - IntroReferral: Introduced in Senate
- 2026-03-02 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S733-734)
- Latest action: 2026-03-02: Introduced in Senate

## Actions

- 2026-03-02 - IntroReferral: Introduced in Senate
- 2026-03-02 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S733-734)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3959",
    "number": "3959",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Smarter Sentencing Act of 2026",
    "type": "S",
    "updateDate": "2026-05-28T19:20:52Z",
    "updateDateIncludingText": "2026-05-28T19:20:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-02",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S733-734)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-02",
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
          "date": "2026-03-02T23:03:40Z",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "UT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "NJ"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "HI"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-02",
      "state": "ME"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "VA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CT"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-03-02",
      "state": "VT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3959is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3959\nIN THE SENATE OF THE UNITED STATES\nMarch 2, 2026 Mr. Durbin (for himself, Mr. Lee , Mr. Booker , Mr. Schatz , Mr. King , Mr. Kaine , Ms. Warren , Mr. Markey , Mr. Blumenthal , Mr. Sanders , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo focus limited Federal resources on the most serious offenders.\n#### 1. Short title\nThis Act may be cited as the Smarter Sentencing Act of 2026 .\n#### 2. Sentencing modifications for certain drug offenses\n##### (a) Controlled Substances Act\nThe Controlled Substances Act ( 21 U.S.C. 801 et seq. ) is amended\u2014\n**(1)**\nin section 102 ( 21 U.S.C. 802 ), by adding at the end the following:\n(61) The term courier means a defendant whose role in the offense was limited to transporting or storing drugs or money. ; and\n**(2)**\nin section 401(b)(1) ( 21 U.S.C. 841(b)(1) )\u2014\n**(A)**\nin subparagraph (A), in the flush text following clause (viii)\u2014\n**(i)**\nby striking 10 years or more and inserting 5 years or more ; and\n**(ii)**\nby striking 15 years and inserting 10 years ; and\n**(B)**\nin subparagraph (B), in the flush text following clause (viii)\u2014\n**(i)**\nby striking 5 years and inserting 2 years ; and\n**(ii)**\nby striking not be less than 10 years and inserting not be less than 5 years .\n##### (b) Controlled Substances Import and Export Act\nSection 1010(b) of the Controlled Substances Import and Export Act ( 21 U.S.C. 960(b) ) is amended\u2014\n**(1)**\nin paragraph (1), in the flush text following subparagraph (H)\u2014\n**(A)**\nby inserting , other than a person who is a courier, after such violation ;\n**(B)**\nby striking person commits and inserting person, other than a courier, commits ; and\n**(C)**\nby inserting If a person who is a courier commits such a violation, the person shall be sentenced to a term of imprisonment of not less than 5 years and not more than life. If a person who is a courier commits such a violation after a prior conviction for a serious drug felony or serious violent felony has become final, the person shall be sentenced to a term of imprisonment of not less than 10 years and not more than life. before Notwithstanding section 3583 ; and\n**(2)**\nin paragraph (2), in the flush text following subparagraph (H)\u2014\n**(A)**\nby inserting , other than a person who is a courier, after such violation ;\n**(B)**\nby striking person commits and inserting person, other than a courier, commits ; and\n**(C)**\nby inserting If a person who is a courier commits such a violation, the person shall be sentenced to a term of imprisonment of not less than 2 years and not more than life. If a person who is a courier commits such a violation after a prior conviction for a serious drug felony or serious violent felony has become final, the person shall be sentenced to a term of imprisonment of not less than 5 years and not more than life. before Notwithstanding section 3583 .\n##### (c) Applicability to Pending and Past Cases\n**(1) Definition**\nIn this subsection, the term covered offense means a violation of a Federal criminal statute, the statutory penalties for which were modified by this section.\n**(2) Pending cases**\nThis section, and the amendments made by this section, shall apply to any sentence imposed after the date of enactment of this Act, regardless of when the offense was committed.\n**(3) Past cases**\nIn the case of a defendant who, before the date of enactment of this Act, was convicted or sentenced for a covered offense, the sentencing court may, on motion of the defendant, the Bureau of Prisons, the attorney for the Government, or on its own motion, impose a reduced sentence after considering the factors set forth in section 3553(a) of title 18, United States Code.\n#### 3. Directive to the Sentencing Commission\n##### (a) Directive to Sentencing Commission\nPursuant to its authority under section 994(p) of title 28, United States Code, and in accordance with this section, the United States Sentencing Commission shall review and amend, if appropriate, its guidelines and its policy statements applicable to persons convicted of an offense under section 401 of the Controlled Substances Act ( 21 U.S.C. 841 ) or section 1010 of the Controlled Substances Import and Export Act ( 21 U.S.C. 960 ) to ensure that the guidelines and policy statements are consistent with the amendments made by section 2 of this Act.\n##### (b) Considerations\nIn carrying out this section, the United States Sentencing Commission shall consider\u2014\n**(1)**\nthe mandate of the United States Sentencing Commission, under section 994(g) of title 28, United States Code, to formulate the sentencing guidelines in such a way as to minimize the likelihood that the Federal prison population will exceed the capacity of the Federal prisons ;\n**(2)**\nthe findings and conclusions of the United States Sentencing Commission in its October 2011 report to Congress entitled, Mandatory Minimum Penalties in the Federal Criminal Justice System;\n**(3)**\nthe fiscal implications of any amendments or revisions to the sentencing guidelines or policy statements made by the United States Sentencing Commission;\n**(4)**\nthe relevant public safety concerns involved in the considerations before the United States Sentencing Commission;\n**(5)**\nthe intent of Congress that penalties for violent, repeat, and serious drug traffickers who present public safety risks remain appropriately severe; and\n**(6)**\nthe need to reduce and prevent racial disparities in Federal sentencing.\n##### (c) Emergency authority\nThe United States Sentencing Commission shall\u2014\n**(1)**\npromulgate the guidelines, policy statements, or amendments provided for in this Act as soon as practicable, and in any event not later than 120 days after the date of enactment of this Act, in accordance with the procedure set forth in section 21(a) of the Sentencing Act of 1987 ( 28 U.S.C. 994 note), as though the authority under that Act had not expired; and\n**(2)**\npursuant to the emergency authority provided under paragraph (1), make such conforming amendments to the Federal sentencing guidelines as the Commission determines necessary to achieve consistency with other guideline provisions and applicable law.\n#### 4. Report by Attorney General\nNot later than 6 months after the date of enactment of this Act, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report outlining how the reduced expenditures on Federal corrections and the cost savings resulting from this Act will be used to help reduce overcrowding in the Federal Bureau of Prisons, help increase proper investment in law enforcement and crime prevention, and help reduce criminal recidivism, thereby increasing the effectiveness of Federal criminal justice spending.\n#### 5. Report on Federal criminal offenses\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term criminal regulatory offense means a Federal regulation that is enforceable by a criminal penalty; and\n**(2)**\nthe term criminal statutory offense means a criminal offense under a Federal statute.\n##### (b) Report on criminal statutory offenses\nNot later than 1 year after the date of enactment of this Act, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report, which shall include\u2014\n**(1)**\na list of all criminal statutory offenses, including a list of the elements for each criminal statutory offense; and\n**(2)**\nfor each criminal statutory offense listed under paragraph (1)\u2014\n**(A)**\nthe potential criminal penalty for the criminal statutory offense;\n**(B)**\nthe number of prosecutions for the criminal statutory offense brought by the Department of Justice each year for the 15-year period preceding the date of enactment of this Act; and\n**(C)**\nthe mens rea requirement for the criminal statutory offense.\n##### (c) Report on criminal regulatory offenses\n**(1) Reports**\nNot later than 1 year after the date of enactment of this Act, the head of each Federal agency described in paragraph (2) shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report, which shall include\u2014\n**(A)**\na list of all criminal regulatory offenses enforceable by the agency; and\n**(B)**\nfor each criminal regulatory offense listed under subparagraph (A)\u2014\n**(i)**\nthe potential criminal penalty for a violation of the criminal regulatory offense;\n**(ii)**\nthe number of violations of the criminal regulatory offense referred to the Department of Justice for prosecution in each of the years during the 15-year period preceding the date of enactment of this Act; and\n**(iii)**\nthe mens rea requirement for the criminal regulatory offense.\n**(2) Agencies described**\nThe Federal agencies described in this paragraph are the Department of Agriculture, the Department of Commerce, the Department of Education, the Department of Energy, the Department of Health and Human Services, the Department of Homeland Security, the Department of Housing and Urban Development, the Department of the Interior, the Department of Labor, the Department of Transportation, the Department of the Treasury, the Commodity Futures Trading Commission, the Consumer Product Safety Commission, the Equal Employment Opportunity Commission, the Export-Import Bank of the United States, the Farm Credit Administration, the Federal Communications Commission, the Federal Deposit Insurance Corporation, the Federal Election Commission, the Federal Labor Relations Authority, the Federal Maritime Commission, the Federal Mine Safety and Health Review Commission, the Federal Trade Commission, the National Labor Relations Board, the National Transportation Safety Board, the Nuclear Regulatory Commission, the Occupational Safety and Health Review Commission, the Office of Congressional Workplace Rights, the Postal Regulatory Commission, the Securities and Exchange Commission, the Securities Investor Protection Corporation, the Environmental Protection Agency, the Small Business Administration, the Federal Housing Finance Agency, and the Office of Government Ethics.\n##### (d) Index\nNot later than 2 years after the date of enactment of this Act\u2014\n**(1)**\nthe Attorney General shall establish a publicly accessible index of each criminal statutory offense listed in the report required under subsection (b) and make the index available and freely accessible on the website of the Department of Justice; and\n**(2)**\nthe head of each agency described in subsection (c)(2) shall establish a publicly accessible index of each criminal regulatory offense listed in the report required under subsection (c)(1) and make the index available and freely accessible on the website of the agency.\n##### (e) Rule of construction\nNothing in this section shall be construed to require or authorize appropriations.",
      "versionDate": "2026-03-02",
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
        "actionDate": "2026-04-14",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 370."
      },
      "number": "2159",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Count the Crimes to Cut Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3868",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Count the Crimes to Cut Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-03-20T18:46:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-02",
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
          "measure-id": "id119s3959",
          "measure-number": "3959",
          "measure-type": "s",
          "orig-publish-date": "2026-03-02",
          "originChamber": "SENATE",
          "update-date": "2026-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3959v00",
            "update-date": "2026-05-28"
          },
          "action-date": "2026-03-02",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Smarter Sentencing Act of 2026</strong></p><p>This bill reduces statutory mandatory minimum penalties for certain drug offenses, requires reporting on the impact of cost savings from the reductions, and establishes a public database of federal criminal offenses.</p><p>First, the bill reduces statutory mandatory minimum penalties for two types of offenders: (1) individuals who manufacture, distribute, or possess with intent to distribute a controlled substance; and (2) couriers who import or export a controlled substance.</p><p>Second, the bill requires the Department of Justice (DOJ) to report on how the reduced expenditures on federal corrections and cost savings from the reductions in mandatory minimum sentences help to reduce overcrowding in federal prisons, increase investment in law enforcement and crime prevention, and reduce recidivism.</p><p>Third, the bill requires DOJ and federal agencies to report on and create public databases of all criminal offenses\u2014criminal statutory offenses and criminal regulatory offenses.</p>"
        },
        "title": "Smarter Sentencing Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3959.xml",
    "summary": {
      "actionDate": "2026-03-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Smarter Sentencing Act of 2026</strong></p><p>This bill reduces statutory mandatory minimum penalties for certain drug offenses, requires reporting on the impact of cost savings from the reductions, and establishes a public database of federal criminal offenses.</p><p>First, the bill reduces statutory mandatory minimum penalties for two types of offenders: (1) individuals who manufacture, distribute, or possess with intent to distribute a controlled substance; and (2) couriers who import or export a controlled substance.</p><p>Second, the bill requires the Department of Justice (DOJ) to report on how the reduced expenditures on federal corrections and cost savings from the reductions in mandatory minimum sentences help to reduce overcrowding in federal prisons, increase investment in law enforcement and crime prevention, and reduce recidivism.</p><p>Third, the bill requires DOJ and federal agencies to report on and create public databases of all criminal offenses\u2014criminal statutory offenses and criminal regulatory offenses.</p>",
      "updateDate": "2026-05-28",
      "versionCode": "id119s3959"
    },
    "title": "Smarter Sentencing Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Smarter Sentencing Act of 2026</strong></p><p>This bill reduces statutory mandatory minimum penalties for certain drug offenses, requires reporting on the impact of cost savings from the reductions, and establishes a public database of federal criminal offenses.</p><p>First, the bill reduces statutory mandatory minimum penalties for two types of offenders: (1) individuals who manufacture, distribute, or possess with intent to distribute a controlled substance; and (2) couriers who import or export a controlled substance.</p><p>Second, the bill requires the Department of Justice (DOJ) to report on how the reduced expenditures on federal corrections and cost savings from the reductions in mandatory minimum sentences help to reduce overcrowding in federal prisons, increase investment in law enforcement and crime prevention, and reduce recidivism.</p><p>Third, the bill requires DOJ and federal agencies to report on and create public databases of all criminal offenses\u2014criminal statutory offenses and criminal regulatory offenses.</p>",
      "updateDate": "2026-05-28",
      "versionCode": "id119s3959"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3959is.xml"
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
      "title": "Smarter Sentencing Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Smarter Sentencing Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to focus limited Federal resources on the most serious offenders.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:23Z"
    }
  ]
}
```
