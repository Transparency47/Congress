# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2688?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2688
- Title: District of Columbia National Guard Home Rule Act
- Congress: 119
- Bill type: S
- Bill number: 2688
- Origin chamber: Senate
- Introduced date: 2025-09-02
- Update date: 2025-12-05T21:37:19Z
- Update date including text: 2025-12-05T21:37:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in Senate
- 2025-09-02 - IntroReferral: Introduced in Senate
- 2025-09-02 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-09-02: Introduced in Senate

## Actions

- 2025-09-02 - IntroReferral: Introduced in Senate
- 2025-09-02 - IntroReferral: Read twice and referred to the Committee on Armed Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2688",
    "number": "2688",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "District of Columbia National Guard Home Rule Act",
    "type": "S",
    "updateDate": "2025-12-05T21:37:19Z",
    "updateDateIncludingText": "2025-12-05T21:37:19Z"
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
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
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
          "date": "2025-09-02T22:33:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NJ"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-09-02",
      "state": "VT"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MD"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "IL"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "VA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "VT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "WI"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2688is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2688\nIN THE SENATE OF THE UNITED STATES\nSeptember 2, 2025 Mr. Van Hollen (for himself, Mr. Booker , Mr. Sanders , Ms. Alsobrooks , Mr. Padilla , Mr. Schiff , Ms. Duckworth , Ms. Warren , Mr. Warner , Mr. Welch , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo extend to the Mayor of the District of Columbia the same authority over the National Guard of the District of Columbia as the Governors of the several States exercise over the National Guard of those States with respect to administration of the National Guard and its use to respond to natural disasters and other civil disturbances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the District of Columbia National Guard Home Rule Act .\n#### 2. Extension of National Guard authorities to Mayor of the District of Columbia\n##### (a) Mayor as Commander-in-Chief\nSection 6 of the Act entitled An Act to provide for the organization of the militia of the District of Columbia, and for other purposes , approved March 1, 1889 (sec. 49\u2013409, D.C. Official Code), is amended by striking President of the United States and inserting Mayor of the District of Columbia .\n##### (b) Reserve corps\nSection 72 of such Act (sec. 49\u2013407, D.C. Official Code) is amended by striking President of the United States each place it appears and inserting Mayor of the District of Columbia .\n##### (c) Appointment of commissioned officers\n**(1)**\nSection 7(a) of such Act (sec. 49\u2013301(a), D.C. Official Code) is amended\u2014\n**(A)**\nby striking President of the United States and inserting Mayor of the District of Columbia ; and\n**(B)**\nby striking President. and inserting Mayor. .\n**(2)**\nSection 9 of such Act (sec. 49\u2013304, D.C. Official Code) is amended by striking President and inserting Mayor of the District of Columbia .\n**(3)**\nSection 13 of such Act (sec. 49\u2013305, D.C. Official Code) is amended by striking President of the United States and inserting Mayor of the District of Columbia .\n**(4)**\nSection 19 of such Act (sec. 49\u2013311, D.C. Official Code) is amended\u2014\n**(A)**\nin subsection (a), by striking to the Secretary of the Army and all that follows through which board and inserting to a board of examination appointed by the Commanding General, which ; and\n**(B)**\nin subsection (b), by striking the Secretary of the Army and all that follows through the period and inserting the Mayor of the District of Columbia, together with any recommendations of the Commanding General. .\n**(5)**\nSection 20 of such Act (sec. 49\u2013312, D.C. Official Code) is amended\u2014\n**(A)**\nby striking President of the United States each place it appears and inserting Mayor of the District of Columbia ; and\n**(B)**\nby striking the President may retire and inserting the Mayor may retire .\n##### (d) Call for duty\n**(1)**\nSection 45 of such Act (sec. 49\u2013103, D.C. Official Code) is amended by striking , or for the United States Marshal and all that follows through shall thereupon order and inserting to order .\n**(2)**\nSection 46 of such Act (sec. 49\u2013104, D.C. Official Code) is amended by striking the President and inserting the Mayor of the District of Columbia .\n##### (e) General courts martial\nSection 51 of such Act (sec. 49\u2013503, D.C. Official Code) is amended by striking the President of the United States and inserting the Mayor of the District of Columbia .\n#### 3. Conforming amendments to title 10 , United States Code\n##### (a) Failure To satisfactorily perform prescribed training\nSection 10148(b) of title 10, United States Code, is amended by striking the commanding general of the District of Columbia National Guard and inserting the Mayor of the District of Columbia .\n##### (b) Appointment of chief of National Guard bureau\nSection 10502(a)(1) of such title is amended by striking the commanding general of the District of Columbia National Guard and inserting the Mayor of the District of Columbia .\n##### (c) Vice chief of National Guard bureau\nSection 10505(a)(1)(A) of such title is amended by striking the commanding general of the District of Columbia National Guard and inserting the Mayor of the District of Columbia .\n##### (d) Other senior National Guard bureau officers\nSection 10506(a)(1) of such title is amended by striking the commanding general of the District of Columbia National Guard both places it appears and inserting the Mayor of the District of Columbia .\n##### (e) Consent for active duty or relocation\n**(1)**\nSection 12301 of such title is amended\u2014\n**(A)**\nin subsection (b), by striking commanding general of the District of Columbia National Guard in the second sentence and inserting Mayor of the District of Columbia ; and\n**(B)**\nin subsection (d), by striking the period at the end and inserting the following: , or, in the case of the District of Columbia National Guard, the Mayor of the District of Columbia. .\n**(2)**\nSection 12406 of such title is amended by striking the commanding general of the National Guard of the District of Columbia and inserting the Mayor of the District of Columbia .\n##### (f) Consent for relocation of units\nSection 18238 of such title is amended by striking the commanding general of the National Guard of the District of Columbia and inserting the Mayor of the District of Columbia .\n#### 4. Conforming amendments to title 32 , United States Code\n##### (a) Maintenance of other troops\nSection 109(c) of title 32, United States Code, is amended by striking (or commanding general in the case of the District of Columbia) .\n##### (b) Drug interdiction and Counter-Drug activities\nSection 112(h)(2) of such title is amended by striking the Commanding General of the National Guard of the District of Columbia and inserting the Mayor of the District of Columbia .\n##### (c) Additional assistance\nSection 113 of such title is amended by adding at the end the following new subsection:\n(e) Inclusion of District of Columbia In this section, the term State includes the District of Columbia. .\n##### (d) Appointment of adjutant general\nSection 314 of such title is amended\u2014\n**(1)**\nby striking subsection (b);\n**(2)**\nby redesignating subsections (c) and (d) as subsections (b) and (c), respectively; and\n**(3)**\nin subsection (b) (as so redesignated), by striking the commanding general of the District of Columbia National Guard in the first sentence and inserting the Mayor of the District of Columbia .\n##### (e) Relief from national guard duty\nSection 325 of such title is amended\u2014\n**(1)**\nin subsection (a)(2)(B), by striking the commanding general of the District of Columbia National Guard and inserting the Mayor of the District of Columbia ; and\n**(2)**\nin subsection (b), by striking the commanding general of the District of Columbia National Guard and inserting the Mayor of the District of Columbia .\n##### (f) Authority To order To perform Active Guard and Reserve duty\n**(1) Authority**\nSubsection (a) of section 328 of such title is amended by striking the commanding general of the District of Columbia National Guard and inserting the Mayor of the District of Columbia .\n**(2) Clerical amendments**\n**(A) Section heading**\nThe heading of such section is amended to read as follows:\n328. Active Guard and Reserve duty: authority of chief executive .\n**(B) Table of sections**\nThe table of sections at the beginning of chapter 3 of such title is amended by striking the item relating to section 328 and inserting the following new item:\n328. Active Guard and Reserve duty: authority of chief executive. .\n##### (g) Personnel matters\nSection 505 of such title is amended by striking the commanding general of the National Guard of the District of Columbia in the first sentence and inserting the Mayor of the District of Columbia .\n##### (h) National Guard challenge program\nSection 509 of such title is amended\u2014\n**(1)**\nin subsection (c)(1), by striking the commanding general of the District of Columbia National Guard, under which the Governor or the commanding general and inserting the Mayor of the District of Columbia, under which the Governor or the Mayor ;\n**(2)**\nin subsection (g)(2), by striking the commanding general of the District of Columbia National Guard and inserting the Mayor of the District of Columbia ;\n**(3)**\nin subsection (j), by striking the commanding general of the District of Columbia National Guard and inserting the Mayor of the District of Columbia ; and\n**(4)**\nin subsection (k), by striking the commanding general of the District of Columbia National Guard in the second sentence and inserting the Mayor of the District of Columbia .\n##### (i) Issuance of supplies\nSection 702(a) of such title is amended by striking the commanding general of the National Guard of the District of Columbia and inserting the Mayor of the District of Columbia .\n##### (j) Appointment of fiscal officer\nSection 708(a) of such title is amended by striking the commanding general of the National Guard of the District of Columbia and inserting the Mayor of the District of Columbia .\n#### 5. Conforming amendment to the District of Columbia Home Rule Act\nSection 602(b) of the District of Columbia Home Rule Act (sec. 1\u2013206.02(b), D.C. Official Code) is amended by striking the National Guard of the District of Columbia, .",
      "versionDate": "2025-09-02",
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
        "actionDate": "2025-09-02",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "5093",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "District of Columbia National Guard Home Rule Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-19T19:20:01Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2688is.xml"
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
      "title": "District of Columbia National Guard Home Rule Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "District of Columbia National Guard Home Rule Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-04T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to extend to the Mayor of the District of Columbia the same authority over the National Guard of the District of Columbia as the Governors of the several States exercise over the National Guard of those States with respect to administration of the National Guard and its use to respond to natural disasters and other civil disturbances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-04T02:03:16Z"
    }
  ]
}
```
