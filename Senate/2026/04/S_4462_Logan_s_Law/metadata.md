# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4462?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4462
- Title: Logan's Law
- Congress: 119
- Bill type: S
- Bill number: 4462
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-15T15:57:27Z
- Update date including text: 2026-05-15T15:57:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4462",
    "number": "4462",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Logan's Law",
    "type": "S",
    "updateDate": "2026-05-15T15:57:27Z",
    "updateDateIncludingText": "2026-05-15T15:57:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T17:49:49Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4462is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4462\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Graham introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a publicly accessible database of individuals with convictions for violent crimes, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as Logan's Law .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Violent Criminal Offender Database\nSec. 101. Definitions.\nSec. 102. Database.\nSec. 103. State participation in database.\nTITLE II\u2014Federal efforts to increase data sharing among States\nSec. 201. Report and recommendations on information sharing.\nI\nViolent Criminal Offender Database\n#### 101. Definitions\nIn this title:\n**(1) Byrne JAG grant program**\nThe term Byrne JAG grant program means the grant program established under subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ).\n**(2) Database**\nThe term Database means the database established under section 102(a).\n**(3) Qualifying conviction**\nThe term qualifying conviction \u2014\n**(A)**\nmeans any conviction for an offense that\u2014\n**(i)**\nis punishable by imprisonment for a term exceeding 180 days, regardless of the sentence actually imposed; and\n**(ii)**\n**(I)**\nhas as an element the use, attempted use, or threatened use of physical force against the person or property of another; or\n**(II)**\nby its nature, involves a substantial risk that physical force against the person or property of another may be used in the course of committing the offense; and\n**(B)**\ndoes not include any conviction\u2014\n**(i)**\nthat has been expunged, vacated, set aside, or otherwise rendered legally inoperative under Federal or State law; or\n**(ii)**\nif the person who committed the offense of conviction has been pardoned for the offense pursuant to a full and unconditional pardon.\n**(4) State**\nThe term State means a State of the United States, the District of Columbia, any commonwealth, territory, or possession of the United States, and a tribal organization.\n**(5) Tribal organization**\nThe term tribal organization has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n#### 102. Database\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall establish a publicly accessible database of all individuals with qualifying convictions, to be known as the Violent Criminal Offender Database .\n##### (b) Requirements\nThe Attorney General shall ensure that\u2014\n**(1)**\nthe Database includes both Federal and State records of qualifying convictions;\n**(2)**\nto the extent practicable, the Database utilizes records collected by the Federal Bureau of Investigation;\n**(3)**\nthe Database is available free of charge to the public;\n**(4)**\nthe Database is searchable by\u2014\n**(A)**\nname;\n**(B)**\naddress;\n**(C)**\ndate of birth;\n**(D)**\nsex;\n**(E)**\nrace;\n**(F)**\nnationality;\n**(G)**\ncitizenship status;\n**(H)**\ntype of conviction;\n**(I)**\ncurrent and historical probation status related to a qualifying conviction, including information on any probation revocation or violation;\n**(J)**\njurisdiction of each qualifying conviction;\n**(K)**\nthe maximum fine and term of imprisonment authorized, and the actual fine and term of imprisonment imposed, for each qualifying conviction;\n**(L)**\nwhether each qualifying conviction was the result of a plea agreement or a trial;\n**(M)**\nthe sentencing judge for each qualifying conviction;\n**(N)**\nthe prosecuting office for each qualifying conviction; and\n**(O)**\nany other searchable category the Attorney General determines appropriate to ensure the safety of the public; and\n**(5)**\nthe public is informed of the availability of the Database.\n##### (c) Updates\n**(1) In general**\nNot less frequently than quarterly, the Attorney General shall update the Database.\n**(2) Removal of persons with legally inoperative convictions**\nUpon determining that a conviction for which a person has been listed in the Database no longer constitutes a qualifying conviction by reason of section 101(3)(B), the Attorney General shall remove the person from the Database with respect to that conviction.\n#### 103. State participation in database\n##### (a) Submission of data\nNot later than 180 days after the date of enactment of this Act, and on an ongoing basis thereafter, each State that receives amounts under the Byrne JAG grant program shall submit to the Attorney General all data regarding qualifying convictions entered by a court of the State or a political subdivision of the State necessary for the Attorney General to comply with section 102.\n##### (b) Byrne JAG grant penalty for noncompliance\nThe Attorney General\u2014\n**(1)**\nshall not distribute amounts under the Bryne JAG grant program to a State that is not in compliance with subsection (a); and\n**(2)**\nin the case of amounts under the Byrne JAG grant program that the Attorney General would have distributed to a State but for the prohibition under paragraph (1) of this subsection, may, at the discretion of the Attorney General, and without regard to the requirements and limitations under section 505 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10156 ), distribute those amounts directly to units of local government in the State, which shall be in addition to the grants required to be made directly to units of local government under subsection (d) of such section 505.\nII\nFederal efforts to increase data sharing among States\n#### 201. Report and recommendations on information sharing\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that includes the following:\n**(1)**\nA description of the current process and procedure for sharing criminal records, including fingerprint, warrant, and criminal history data\u2014\n**(A)**\nbetween the States; and\n**(B)**\nbetween the States and the Federal Government.\n**(2)**\nThe identification of any procedural or process burdens that can or could result in criminal records not being shared between prosecutorial offices or departments, to the extent that such burdens result in harm to the public.\n**(3)**\nRecommendations for both the Department of Justice and Congress to ensure that criminal records are shared between relevant prosecutorial offices and law enforcement agencies of States and between such offices and agencies of States and the Federal Government such that the public is protected from criminal offenders.\n**(4)**\nAny other matters, issues, laws, compacts, or regulations that the Attorney General identifies as detrimental to the goal of ensuring that\u2014\n**(A)**\nthe records of criminal offenders are shared with prosecutors nationwide; and\n**(B)**\nrepeat criminal offenders are not given inappropriately light sentences due to their records not being shared as described in subparagraph (A).",
      "versionDate": "2026-04-30",
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
        "actionDate": "2026-04-30",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "8611",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Logan's Law",
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
        "updateDate": "2026-05-15T15:57:27Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4462is.xml"
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
      "title": "Logan's Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-09T05:23:45Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Logan's Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-09T05:23:43Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a publicly accessible database of individuals with convictions for violent crimes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-09T05:18:30Z"
    }
  ]
}
```
