# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1734?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1734
- Title: Justice for Angel Families Act
- Congress: 119
- Bill type: S
- Bill number: 1734
- Origin chamber: Senate
- Introduced date: 2025-05-13
- Update date: 2025-12-05T21:57:45Z
- Update date including text: 2025-12-05T21:57:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in Senate
- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-13: Introduced in Senate

## Actions

- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1734",
    "number": "1734",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Justice for Angel Families Act",
    "type": "S",
    "updateDate": "2025-12-05T21:57:45Z",
    "updateDateIncludingText": "2025-12-05T21:57:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-13",
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
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T18:52:03Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NC"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "ND"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1734is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1734\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2025 Mr. Marshall (for himself, Mr. Budd , Mr. Cramer , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize grants for crime victims to be distributed to angel families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for Angel Families Act .\n#### 2. Grants for angel families\nSection 1403 of the Victims of Crime Act of 1984 ( 34 U.S.C. 20102 ) is amended\u2014\n**(1)**\nin subsection (b), by amending paragraph (1) to read as follows:\n(1) such program is operated by a State and offers compensation to\u2014 (A) victims and survivors of victims of criminal violence, including drunk driving and domestic violence, for\u2014 (i) medical expenses attributable to a physical injury resulting from a compensable crime, including expenses for mental health counseling and care; (ii) loss of wages attributable to a physical injury resulting from a compensable crime; and (iii) funeral expenses attributable to a death resulting from a compensable crime; or (B) angel families for\u2014 (i) medical expenses attributable to any injury resulting from a compensable crime, including expenses for mental health counseling and care; (ii) loss of wages attributable to emotional distress resulting from a compensable crime; and (iii) funeral expenses attributable to a death resulting from a compensable crime; ; and\n**(2)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (4), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(6) the term angel family means the immediate family members of any individual who is a victim of homicide committed by\u2014 (A) an alien described in section 212(a)(6)(A)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(6)(A)(i) ) who is unlawfully present in the United States; or (B) any member of an international criminal organization involved in the unlawful trafficking of controlled substances (as defined in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 )), including an international drug cartel. .\n#### 3. Victims of Immigration Crime Engagement Office\n##### (a) Establishment\nTitle I of the Homeland Security Act of 2002 ( 6 U.S.C. 111 et seq. ) is amended by adding at the end the following:\n104. Victims of Immigration Crime Engagement Office (a) Definitions In this section: (1) Alien The term alien means an individual who\u2014 (A) is described in section 212(a)(6)(A)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(6)(A)(i) ); and (B) is unlawfully present in the United States. (2) Director The term Director means the Director of the Victims of Immigration Crime Engagement Office established pursuant to subsection (b). (b) In general The Secretary shall establish, within the Office of the Secretary, the Victims of Immigration Crime Engagement Office to provide proactive, timely, and professional services to victims of crimes committed by aliens who are inadmissible under section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ), deportable under section 237(a) of such Act ( 8 U.S.C. 1227(a) ), or otherwise unlawfully present in the United States, and to the family members of such victims. (c) Duties The Office shall be headed by a Director, who shall\u2014 (1) create a hotline for victims described in subsection (b) and for the family members of such victims\u2014 (A) to ensure that such victims and family members receive the support they need, including by\u2014 (i) providing information available to help victims and their family members understand the immigration enforcement and removal process; (ii) liaising with social service professionals to assist in providing support services referral information; and (iii) directing victims and their family members to a wide range of available resources; (B) to assist victims and family members of victims to register for automated custody status information related to the criminal alien; (C) to provide victims and their family members with releasable criminal or immigration history about the criminal alien; and (D) to provide immediate services to victims and their family members and collect metrics and information to determine additional resource needs and how to improve services to victims; and (2) conduct a case study on providing proactive, timely, and professional services to victims of crimes, and the family members of such victims, that are committed by aliens who are inadmissible under section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ), deportable under section 237(a) of such Act ( 8 U.S.C. 1227(a) ), or otherwise unlawfully present in the United States. (d) Annual report Not later than 1 year after the date of the enactment of the Justice for Angel Families Act , and annually thereafter, the Director shall submit to Congress a report regarding the impact on victims of crimes committed by aliens who are inadmissible under section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ), deportable under section 237(a) of such Act ( 8 U.S.C. 1227(a) ), or otherwise unlawfully present in the United States that includes\u2014 (1) a summary of the case study described in subsection (c)(2); and (2) information regarding\u2014 (A) the demographics of such victims and criminal aliens; (B) the locations of such crimes; (C) the type of crimes committed; and (D) whether the criminal aliens have committed multiple crimes. .\n##### (b) Clerical amendment\nThe table of contents of the Homeland Security Act of 2002 ( 6 U.S.C. 101 et seq. ) is amended by inserting after the item relating to section 103 the following:\nSec. 104. Victims of Immigration Crime Engagement Office. .",
      "versionDate": "2025-05-13",
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
        "actionDate": "2025-05-13",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3362",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Justice for Angel Families Act",
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
        "updateDate": "2025-05-28T13:09:21Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1734is.xml"
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
      "title": "Justice for Angel Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Justice for Angel Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize grants for crime victims to be distributed to angel families, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:48Z"
    }
  ]
}
```
