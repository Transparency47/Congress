# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2686?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2686
- Title: DC CRIMES Act
- Congress: 119
- Bill type: S
- Bill number: 2686
- Origin chamber: Senate
- Introduced date: 2025-09-02
- Update date: 2025-09-22T19:28:49Z
- Update date including text: 2025-09-22T19:28:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in Senate
- 2025-09-02 - IntroReferral: Introduced in Senate
- 2025-09-02 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-09-02: Introduced in Senate

## Actions

- 2025-09-02 - IntroReferral: Introduced in Senate
- 2025-09-02 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2686",
    "number": "2686",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "DC CRIMES Act",
    "type": "S",
    "updateDate": "2025-09-22T19:28:49Z",
    "updateDateIncludingText": "2025-09-22T19:28:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-02",
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
          "date": "2025-09-02T20:52:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "AR"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "LA"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "MT"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NC"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "TN"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2686is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2686\nIN THE SENATE OF THE UNITED STATES\nSeptember 2, 2025 Mr. Banks (for himself, Mr. Cotton , Mr. Cassidy , Mr. Sheehy , Mr. Budd , and Mr. Hagerty ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo limit youth offender status in the District of Columbia to individuals 18 years of age or younger, to direct the Attorney General for the District of Columbia to establish and operate a publicly accessible website containing updated statistics on juvenile crime in the District of Columbia, to amend the District of Columbia Home Rule Act to prohibit the Council of the District of Columbia from enacting changes to existing criminal liability sentences, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the DC Criminal Reforms to Immediately Make Everyone Safe Act or the DC CRIMES Act .\n#### 2. Youth offenders\n##### (a) Limiting youth offender status in District of Columbia to individuals 18 years of age or younger\n**(1) Limitation**\nSection 2(6) of the Youth Rehabilitation Amendment Act of 1985 (sec. 24\u2013901(6), D.C. Official Code) is amended by striking 24 years of age or younger and inserting 18 years of age or younger .\n**(2) Conforming amendments**\n**(A) Repeal consideration of individuals 18 through 24 years of age in strategic plan for facilities, treatment, and services**\nSection 3(a\u20131) of such Act (sec. 24\u2013902(a\u20131), D.C. Official Code) is amended by striking paragraph (3).\n**(B) Community service for individuals under order of probation**\nSection 4(a)(2) of such Act (sec. 24\u2013903(a)(2), D.C. Official Code) is amended by striking 15 to 24 years of age and inserting 15 to 18 years of age .\n##### (b) Prohibiting issuance of sentence less than mandatory-Minimum term\nSection 4(b) of such Act (sec. 24\u2013903(b), D.C. Official Code) is amended\u2014\n**(1)**\nby striking paragraph (2); and\n**(2)**\nby redesignating paragraph (3) as paragraph (2).\n#### 3. Establishment and operation of website on District of Columbia juvenile crime statistics\n##### (a) Establishment and operation\n**(1) In general**\nSubchapter I of chapter 23 of title 16, District of Columbia Official Code, is amended by adding at the end the following new section:\n16\u20132340.01. Website of updated statistics on juvenile crime (a) Establishment and operation of website The Attorney General for the District of Columbia shall establish and operate a publicly accessible website that contains data on juvenile crime in the District of Columbia, including each of the following statistical measures: (1) The total number of juveniles arrested each year. (2) The total number and percentage of juveniles arrested each year, broken down by age, race, and sex. (3) Of the total number of juveniles arrested each year, the total number and percentage arrested for petty crime, including the following crimes: (A) Vandalism. (B) Theft. (C) Shoplifting. (4) Of the total number of juveniles arrested each year, the total number and percentage arrested for a crime of violence (as defined in section 23\u20131331(4)). (5) Of the total number of juveniles arrested each year, the total number and percentage who were arrested for their first offense. (6) Of the total number of juveniles arrested each year, the total number and percentage who had been arrested previously. (7) Of the total number of juveniles arrested each year who had been arrested previously\u2014 (A) the total number of previous arrests; and (B) the percentage of juveniles who had 1, 2, 3, or more than 3 previous arrests. (8) Of the total number of juveniles arrested each year, the declination rate for prosecutions by the Office of the Attorney General for the District of Columbia. (9) Of the total number of juveniles sentenced each year, the number and percentage who were tried as adults. (10) Of the total number of juveniles prosecuted each year, the number and percentage who were not sentenced, who were sentenced to a misdemeanor, and who were sentenced to a felony. (11) Of the total number of juveniles sentenced each year, the number and percentage of juveniles sentenced to\u2014 (A) 0 to 3 months; (B) 4 to 6 months; (C) 6 to 12 months; (D) 12 to 24 months; or (E) not less than 24 months. (b) Updates The Attorney General shall update the information contained on the website established under subsection (a) on a monthly basis. (c) Maintaining archive of information The Attorney General shall ensure that the information contained on the website established under subsection (a) is archived appropriately to provide indefinite public access to historical data of juvenile arrests and prosecutions. (d) Format The Attorney General shall ensure that the information contained on the website established under subsection (a), including historical data described in subsection (c), is available in a machine-readable format available for bulk download. (e) Prohibiting disclosure of personally identifiable information In carrying out this section, the Attorney General shall ensure that the website established under subsection (a) does not include the personally identifiable information of any juvenile. (f) Definitions In this section\u2014 (1) the term crime has the meaning given the term offense in section 23\u20131331(2); and (2) the term juvenile has the meaning given the term youth offender in section 2(6) of the Youth Rehabilitation Amendment Act of 1985 (sec. 24\u2013901(6), D.C. Official Code). .\n**(2) Technical and conforming amendment**\nThe table of contents for chapter 23 of title 16, District of Columbia Official Code, is amended by inserting after the section designation relating to section 16\u20132340 the following:\n16\u20132340.01. Website of updated statistics on juvenile crime. .\n##### (b) Conforming amendments relating to authorized release of information\n**(1) Juvenile case records of Family Court**\nSection 16\u20132331, District of Columbia Official Code, is amended\u2014\n**(A)**\nby redesignating subsection (i) as subsection (j); and\n**(B)**\nby inserting after subsection (h\u20132) the following new subsection:\n(i) Notwithstanding subsection (b) of this section, the Attorney General may inspect juvenile case records for purposes of the website established and operated under section 16\u20132340.01. .\n**(2) Juvenile social records of Family Court**\nSection 16\u20132332, District of Columbia Official Code, is amended\u2014\n**(A)**\nby redesignating subsection (h) as subsection (i); and\n**(B)**\nby inserting after subsection (g) the following new subsection:\n(h) Notwithstanding subsection (b) of this section, the Attorney General may inspect juvenile social records for purposes of the website established and operated under section 16\u20132340.01. .\n**(3) Police and other law enforcement records**\nSection 16\u20132333, District of Columbia Official Code, is amended\u2014\n**(A)**\nby redesignating subsection (g) as subsection (h); and\n**(B)**\nby inserting after subsection (f) the following new subsection:\n(g) Notwithstanding subsection (a) of this section, the Attorney General may inspect law enforcement records and files concerning a child for purposes of the website established and operated under section 16\u20132340.01. .\n##### (c) Effective date\nThe Attorney General for the District of Columbia shall establish the website under section 16\u20132340.01, District of Columbia Official Code, as added by subsection (a), not later than 180 days after the date of the enactment of this Act.\n#### 4. Prohibiting Council from enacting changes to existing criminal sentences\nSection 602(a) of the District of Columbia Home Rule Act (sec. 1\u2013206.02(a), D.C. Official Code) is amended\u2014\n**(1)**\nin paragraph (9), by striking or at the end;\n**(2)**\nin paragraph (10), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following new paragraph:\n(11) enact any act, resolution, or rule to change any mandatory minimum sentence or criminal sentencing guideline in effect on the date of the enactment of the DC CRIMES Act . .",
      "versionDate": "2025-09-02",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-22T19:28:49Z"
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
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2686is.xml"
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
      "title": "DC CRIMES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-10T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DC CRIMES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-05T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DC Criminal Reforms to Immediately Make Everyone Safe Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-05T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to limit youth offender status in the District of Columbia to individuals 18 years of age or younger, to direct the Attorney General for the District of Columbia to establish and operate a publicly accessible website containing updated statistics on juvenile crime in the District of Columbia, to amend the District of Columbia Home Rule Act to prohibit the Council of the District of Columbia from enacting changes to existing criminal liability sentences, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-05T04:03:22Z"
    }
  ]
}
```
