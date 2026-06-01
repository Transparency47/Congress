# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/633?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/633
- Title: TAKE IT DOWN Act
- Congress: 119
- Bill type: HR
- Bill number: 633
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2025-11-18T09:00:04Z
- Update date including text: 2025-11-18T09:00:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-04-08 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-08 - Committee: Ordered to be Reported by the Yeas and Nays: 49 - 1.
- 2025-04-28 - Calendars: Placed on the Union Calendar, Calendar No. 59.
- 2025-04-28 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-82.
- 2025-04-28 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-82.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-04-08 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-08 - Committee: Ordered to be Reported by the Yeas and Nays: 49 - 1.
- 2025-04-28 - Calendars: Placed on the Union Calendar, Calendar No. 59.
- 2025-04-28 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-82.
- 2025-04-28 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-82.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/633",
    "number": "633",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S000168",
        "district": "27",
        "firstName": "Maria",
        "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
        "lastName": "Salazar",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "TAKE IT DOWN Act",
    "type": "HR",
    "updateDate": "2025-11-18T09:00:04Z",
    "updateDateIncludingText": "2025-11-18T09:00:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 59.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-82.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-82.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 49 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
            "date": "2025-04-28T16:38:34Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-08T19:23:26Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-22T15:00:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "PA"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MI"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "VI"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NJ"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NV"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "OK"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NJ"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "CO"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "LA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "SC"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MS"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "AZ"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "GA"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "CO"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "NY"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "NC"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NC"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "ID"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "DE"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MN"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "ND"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr633ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 633\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Ms. Salazar (for herself, Ms. Dean of Pennsylvania , Mr. Pfluger , Mrs. Dingell , Mr. Buchanan , and Ms. Plaskett ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require covered platforms to remove nonconsensual intimate visual depictions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tools to Address Known Exploitation by Immobilizing Technological Deepfakes On Websites and Networks Act or the TAKE IT DOWN Act .\n#### 2. Criminal prohibition on intentional disclosure of nonconsensual intimate visual depictions\n##### (a) In general\nSection 223 of the Communications Act of 1934 ( 47 U.S.C. 223 ) is amended\u2014\n**(1)**\nby redesignating subsection (h) as subsection (i); and\n**(2)**\nby inserting after subsection (g) the following:\n(h) Intentional disclosure of nonconsensual intimate visual depictions (1) Definitions In this subsection: (A) Consent The term consent means an affirmative, conscious, and voluntary authorization made by an individual free from force, fraud, duress, misrepresentation, or coercion. (B) Digital forgery The term digital forgery means any intimate visual depiction of an identifiable individual created through the use of software, machine learning, artificial intelligence, or any other computer-generated or technological means, including by adapting, modifying, manipulating, or altering an authentic visual depiction, that, when viewed as a whole by a reasonable person, is indistinguishable from an authentic visual depiction of the individual. (C) Identifiable individual The term identifiable individual means an individual\u2014 (i) who appears in whole or in part in an intimate visual depiction; and (ii) whose face, likeness, or other distinguishing characteristic (including a unique birthmark or other recognizable feature) is displayed in connection with such intimate visual depiction. (D) Interactive computer service The term interactive computer service has the meaning given the term in section 230. (E) Intimate visual depiction The term intimate visual depiction has the meaning given such term in section 1309 of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851 ). (F) Minor The term minor means any individual under the age of 18 years. (2) Offense involving authentic intimate visual depictions (A) Involving adults Except as provided in subparagraph (C), it shall be unlawful for any person, in interstate or foreign commerce, to use an interactive computer service to knowingly publish an intimate visual depiction of an identifiable individual who is not a minor if\u2014 (i) the intimate visual depiction was obtained or created under circumstances in which the person knew or reasonably should have known the identifiable individual had a reasonable expectation of privacy; (ii) what is depicted was not voluntarily exposed by the identifiable individual in a public or commercial setting; (iii) what is depicted is not a matter of public concern; and (iv) publication of the intimate visual depiction\u2014 (I) is intended to cause harm; or (II) causes harm, including psychological, financial, or reputational harm, to the identifiable individual. (B) Involving minors Except as provided in subparagraph (C), it shall be unlawful for any person, in interstate or foreign commerce, to use an interactive computer service to knowingly publish an intimate visual depiction of an identifiable individual who is a minor with intent to\u2014 (i) abuse, humiliate, harass, or degrade the minor; or (ii) arouse or gratify the sexual desire of any person. (C) Exceptions Subparagraphs (A) and (B) shall not apply to\u2014 (i) a lawfully authorized investigative, protective, or intelligence activity of\u2014 (I) a law enforcement agency of the United States, a State, or a political subdivision of a State; or (II) an intelligence agency of the United States; (ii) a disclosure made reasonably and in good faith\u2014 (I) to a law enforcement officer or agency; (II) as part of a document production or filing associated with a legal proceeding; (III) as part of medical education, diagnosis, or treatment or for a legitimate medical, scientific, or education purpose; (IV) in the reporting of unlawful content or unsolicited or unwelcome conduct or in pursuance of a legal, professional, or other lawful obligation; or (V) to seek support or help with respect to the receipt of an unsolicited intimate visual depiction; (iii) a disclosure reasonably intended to assist the identifiable individual; (iv) a person who possesses or publishes an intimate visual depiction of himself or herself engaged in nudity or sexually explicit conduct (as that term is defined in section 2256(2)(A) of title 18, United States Code); or (v) the publication of an intimate visual depiction that constitutes\u2014 (I) child pornography (as that term is defined in section 2256 of title 18, United States Code); or (II) a visual depiction described in subsection (a) or (b) of section 1466A of title 18, United States Code (relating to obscene visual representations of the sexual abuse of children). (3) Offense involving digital forgeries (A) Involving adults Except as provided in subparagraph (C), it shall be unlawful for any person, in interstate or foreign commerce, to use an interactive computer service to knowingly publish a digital forgery of an identifiable individual who is not a minor if\u2014 (i) the digital forgery was published without the consent of the identifiable individual; (ii) what is depicted was not voluntarily exposed by the identifiable individual in a public or commercial setting; (iii) what is depicted is not a matter of public concern; and (iv) publication of the digital forgery\u2014 (I) is intended to cause harm; or (II) causes harm, including psychological, financial, or reputational harm, to the identifiable individual. (B) Involving minors Except as provided in subparagraph (C), it shall be unlawful for any person, in interstate or foreign commerce, to use an interactive computer service to knowingly publish a digital forgery of an identifiable individual who is a minor with intent to\u2014 (i) abuse, humiliate, harass, or degrade the minor; or (ii) arouse or gratify the sexual desire of any person. (C) Exceptions Subparagraphs (A) and (B) shall not apply to\u2014 (i) a lawfully authorized investigative, protective, or intelligence activity of\u2014 (I) a law enforcement agency of the United States, a State, or a political subdivision of a State; or (II) an intelligence agency of the United States; (ii) a disclosure made reasonably and in good faith\u2014 (I) to a law enforcement officer or agency; (II) as part of a document production or filing associated with a legal proceeding; (III) as part of medical education, diagnosis, or treatment or for a legitimate medical, scientific, or education purpose; (IV) in the reporting of unlawful content or unsolicited or unwelcome conduct or in pursuance of a legal, professional, or other lawful obligation; or (V) to seek support or help with respect to the receipt of an unsolicited intimate visual depiction; (iii) a disclosure reasonably intended to assist the identifiable individual; (iv) a person who possesses or publishes a digital forgery of himself or herself engaged in nudity or sexually explicit conduct (as that term is defined in section 2256(2)(A) of title 18, United States Code); or (v) the publication of an intimate visual depiction that constitutes\u2014 (I) child pornography (as that term is defined in section 2256 of title 18, United States Code); or (II) a visual depiction described in subsection (a) or (b) of section 1466A of title 18, United States Code (relating to obscene visual representations of the sexual abuse of children). (4) Penalties (A) Offenses involving adults Any person who violates paragraph (2)(A) or (3)(A) shall be fined under title 18, United States Code, imprisoned not more than 2 years, or both. (B) Offenses involving minors Any person who violates paragraph (2)(B) or (3)(B) shall be fined under title 18, United States Code, imprisoned not more than 3 years, or both. (5) Rules of construction For purposes of paragraphs (2) and (3)\u2014 (A) the fact that the identifiable individual provided consent for the creation of the intimate visual depiction shall not establish that the individual provided consent for the publication of the intimate visual depiction; and (B) the fact that the identifiable individual disclosed the intimate visual depiction to another individual shall not establish that the identifiable individual provided consent for the publication of the intimate visual depiction by the person alleged to have violated paragraph (2) or (3), respectively. (6) Threats (A) Threats involving authentic intimate visual depictions Any person who intentionally threatens to commit an offense under paragraph (2) for the purpose of intimidation, coercion, extortion, or to create mental distress shall be punished as provided in paragraph (4). (B) Threats involving digital forgeries (i) Threats involving adults Any person who intentionally threatens to commit an offense under paragraph (3)(A) for the purpose of intimidation, coercion, extortion, or to create mental distress shall be fined under title 18, United States Code, imprisoned not more than 18 months, or both. (ii) Threats involving minors Any person who intentionally threatens to commit an offense under paragraph (3)(B) for the purpose of intimidation, coercion, extortion, or to create mental distress shall be fined under title 18, United States Code, imprisoned not more than 30 months, or both. (7) Forfeiture (A) In general The court, in imposing a sentence on any person convicted of a violation of paragraph (2) or (3), shall order, in addition to any other sentence imposed and irrespective of any provision of State law, that the person forfeit to the United States\u2014 (i) any material distributed in violation of that paragraph; (ii) the person\u2019s interest in property, real or personal, constituting or derived from any gross proceeds of the violation, or any property traceable to such property, obtained or retained directly or indirectly as a result of the violation; and (iii) any personal property of the person used, or intended to be used, in any manner or part, to commit or to facilitate the commission of the violation. (B) Procedures Section 413 of the Controlled Substances Act ( 21 U.S.C. 853 ), with the exception of subsections (a) and (d), shall apply to the criminal forfeiture of property under subparagraph (A). (8) Restitution The court shall order restitution for an offense under paragraph (2) or (3) in the same manner as under section 2264 of title 18, United States Code. (9) Rule of construction Nothing in this subsection shall be construed to limit the application of any other relevant law, including section 2252 of title 18, United States Code. .\n##### (b) Defenses\nSection 223(e)(1) of the Communications Act of 1934 ( 47 U.S.C. 223(e)(1) ) is amended by striking or (d) and inserting , (d), or (h) .\n##### (c) Technical and conforming amendment\nSubsection (i) of section 223 of the Communications Act of 1934 ( 47 U.S.C. 223 ), as so redesignated by subsection (a), is amended by inserting Definitions .\u2014 before For purposes of this section .\n#### 3. Notice and removal of nonconsensual intimate visual depictions\n##### (a) In general\n**(1) Notice and removal process**\n**(A) Establishment**\nNot later than 1 year after the date of enactment of this Act, a covered platform shall establish a process whereby an identifiable individual (or an authorized person acting on behalf of such individual) may\u2014\n**(i)**\nnotify the covered platform of an intimate visual depiction published on the covered platform that\u2014\n**(I)**\nincludes a depiction of the identifiable individual; and\n**(II)**\nwas published without the consent of the identifiable individual; and\n**(ii)**\nsubmit a request for the covered platform to remove such intimate visual depiction.\n**(B) Requirements**\nA notification and request for removal of an intimate visual depiction submitted under the process established under subparagraph (A) shall include, in writing\u2014\n**(i)**\na physical or electronic signature of the identifiable individual (or an authorized person acting on behalf of such individual);\n**(ii)**\nan identification of, and information reasonably sufficient for the covered platform to locate, the intimate visual depiction of the identifiable individual;\n**(iii)**\na brief statement that the identifiable individual has a good faith belief that any intimate visual depiction identified under clause (ii) is not consensual, including any relevant information for the covered platform to determine the intimate visual depiction was published without the consent of the identifiable individual; and\n**(iv)**\ninformation sufficient to enable the covered platform to contact the identifiable individual (or an authorized person acting on behalf of such individual).\n**(2) Notice of process**\nA covered platform shall provide on the platform a clear and conspicuous notice, which may be provided through a clear and conspicuous link to another web page or disclosure, of the notice and removal process established under paragraph (1)(A) that\u2014\n**(A)**\nis easy to read and in plain language; and\n**(B)**\nprovides information regarding the responsibilities of the covered platform under this section, including a description of how an individual can submit a notification and request for removal.\n**(3) Removal of nonconsensual intimate visual depictions**\nUpon receiving a valid removal request from an identifiable individual (or an authorized person acting on behalf of such individual) using the process described in paragraph (1)(A)(ii), a covered platform shall, as soon as possible, but not later than 48 hours after receiving such request\u2014\n**(A)**\nremove the intimate visual depiction; and\n**(B)**\nmake reasonable efforts to identify and remove any known identical copies of such depiction.\n**(4) Limitation on liability**\nA covered platform shall not be liable for any claim based on the covered platform\u2019s good faith disabling of access to, or removal of, material claimed to be a nonconsensual intimate visual depiction based on facts or circumstances from which the unlawful publishing of an intimate visual depiction is apparent, regardless of whether the intimate visual depiction is ultimately determined to be unlawful or not.\n##### (b) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA failure to reasonably comply with the notice and takedown obligations under subsection (a) shall be treated as a violation of a rule defining an unfair or a deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nExcept as provided in subparagraph (D), the Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Federal Trade Commission under any other provision of law.\n**(D) Scope of jurisdiction**\nNotwithstanding section 4, 5(a)(2), or 6 of the Federal Trade Commission Act ( 15 U.S.C. 44 , 45(a)(2), 46), or any jurisdictional limitation of the Commission, the Commission shall also enforce this section in the same manner provided in subparagraph (A), with respect to organizations that are not organized to carry on business for their own profit or that of their members.\n#### 4. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Consent; digital forgery; identifiable individual; intimate visual depiction**\nThe terms consent , digital forgery , identifiable individual , intimate visual depiction , and minor have the meaning given such terms in section 223(h) of the Communications Act of 1934 ( 47 U.S.C. 223 ), as added by section 2.\n**(3) Covered platform**\n**(A) In general**\nThe term covered platform means a website, online service, online application, or mobile application\u2014\n**(i)**\nthat serves the public; and\n**(ii)**\n**(I)**\nthat primarily provides a forum for user-generated content, including messages, videos, images, games, and audio files; or\n**(II)**\nfor which it is in the regular course of trade or business of the website, online service, online application, or mobile application to publish, curate, host, or make available content of nonconsensual intimate visual depictions.\n**(B) Exclusions**\nThe term covered platform shall not include the following:\n**(i)**\nA provider of broadband internet access service (as described in section 8.1(b) of title 47, Code of Federal Regulations, or successor regulation).\n**(ii)**\nElectronic mail.\n**(iii)**\nExcept as provided in subparagraph (A)(ii)(II), an online service, application, or website\u2014\n**(I)**\nthat consists primarily of content that is not user generated but is preselected by the provider of such online service, application, or website; and\n**(II)**\nfor which any chat, comment, or interactive functionality is incidental to, directly related to, or dependent on the provision of the content described in subclause (I).\n#### 5. Severability\nIf any provision of this Act, or an amendment made by this Act, is determined to be unenforceable or invalid, the remaining provisions of this Act and the amendments made by this Act shall not be affected.",
      "versionDate": "2025-01-22",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr633rh.xml",
      "text": "IB\nUnion Calendar No. 59\n119th CONGRESS\n1st Session\nH. R. 633\n[Report No. 119\u201382]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Ms. Salazar (for herself, Ms. Dean of Pennsylvania , Mr. Pfluger , Mrs. Dingell , Mr. Buchanan , and Ms. Plaskett ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nApril 28, 2025 Additional sponsors: Ms. De La Cruz , Mr. Costa , Mr. Smith of New Jersey , Ms. Lee of Nevada , Mr. Khanna , Mrs. Bice , Mr. Kean , Mr. Suozzi , Mr. Goldman of Texas , Ms. Boebert , Mr. Crenshaw , Mr. Higgins of Louisiana , Mr. Wilson of South Carolina , Mr. Meuser , Mr. Van Drew , Mr. Nunn of Iowa , Mr. Guest , Mr. Hamadeh of Arizona , Mr. Carter of Georgia , Mr. Hurd of Colorado , Mr. Williams of Texas , Ms. Malliotakis , Mr. Edwards , Mr. Carbajal , Mr. Fitzpatrick , Mr. Bresnahan , Mr. Harrigan , Mr. LaLota , Mr. Fulcher , Ms. McBride , Mr. Gooden , Mr. Cuellar , Ms. Craig , Mr. Obernolte , Ms. Fedorchak , and Mr. Mackenzie\nApril 28, 2025 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo require covered platforms to remove nonconsensual intimate visual depictions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tools to Address Known Exploitation by Immobilizing Technological Deepfakes On Websites and Networks Act or the TAKE IT DOWN Act .\n#### 2. Criminal prohibition on intentional disclosure of nonconsensual intimate visual depictions\n##### (a) In general\nSection 223 of the Communications Act of 1934 ( 47 U.S.C. 223 ) is amended\u2014\n**(1)**\nby redesignating subsection (h) as subsection (i); and\n**(2)**\nby inserting after subsection (g) the following:\n(h) Intentional disclosure of nonconsensual intimate visual depictions (1) Definitions In this subsection: (A) Consent The term consent means an affirmative, conscious, and voluntary authorization made by an individual free from force, fraud, duress, misrepresentation, or coercion. (B) Digital forgery The term digital forgery means any intimate visual depiction of an identifiable individual created through the use of software, machine learning, artificial intelligence, or any other computer-generated or technological means, including by adapting, modifying, manipulating, or altering an authentic visual depiction, that, when viewed as a whole by a reasonable person, is indistinguishable from an authentic visual depiction of the individual. (C) Identifiable individual The term identifiable individual means an individual\u2014 (i) who appears in whole or in part in an intimate visual depiction; and (ii) whose face, likeness, or other distinguishing characteristic (including a unique birthmark or other recognizable feature) is displayed in connection with such intimate visual depiction. (D) Interactive computer service The term interactive computer service has the meaning given the term in section 230. (E) Intimate visual depiction The term intimate visual depiction has the meaning given such term in section 1309 of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851 ). (F) Minor The term minor means any individual under the age of 18 years. (2) Offense involving authentic intimate visual depictions (A) Involving adults Except as provided in subparagraph (C), it shall be unlawful for any person, in interstate or foreign commerce, to use an interactive computer service to knowingly publish an intimate visual depiction of an identifiable individual who is not a minor if\u2014 (i) the intimate visual depiction was obtained or created under circumstances in which the person knew or reasonably should have known the identifiable individual had a reasonable expectation of privacy; (ii) what is depicted was not voluntarily exposed by the identifiable individual in a public or commercial setting; (iii) what is depicted is not a matter of public concern; and (iv) publication of the intimate visual depiction\u2014 (I) is intended to cause harm; or (II) causes harm, including psychological, financial, or reputational harm, to the identifiable individual. (B) Involving minors Except as provided in subparagraph (C), it shall be unlawful for any person, in interstate or foreign commerce, to use an interactive computer service to knowingly publish an intimate visual depiction of an identifiable individual who is a minor with intent to\u2014 (i) abuse, humiliate, harass, or degrade the minor; or (ii) arouse or gratify the sexual desire of any person. (C) Exceptions Subparagraphs (A) and (B) shall not apply to\u2014 (i) a lawfully authorized investigative, protective, or intelligence activity of\u2014 (I) a law enforcement agency of the United States, a State, or a political subdivision of a State; or (II) an intelligence agency of the United States; (ii) a disclosure made reasonably and in good faith\u2014 (I) to a law enforcement officer or agency; (II) as part of a document production or filing associated with a legal proceeding; (III) as part of medical education, diagnosis, or treatment or for a legitimate medical, scientific, or education purpose; (IV) in the reporting of unlawful content or unsolicited or unwelcome conduct or in pursuance of a legal, professional, or other lawful obligation; or (V) to seek support or help with respect to the receipt of an unsolicited intimate visual depiction; (iii) a disclosure reasonably intended to assist the identifiable individual; (iv) a person who possesses or publishes an intimate visual depiction of himself or herself engaged in nudity or sexually explicit conduct (as that term is defined in section 2256(2)(A) of title 18, United States Code); or (v) the publication of an intimate visual depiction that constitutes\u2014 (I) child pornography (as that term is defined in section 2256 of title 18, United States Code); or (II) a visual depiction described in subsection (a) or (b) of section 1466A of title 18, United States Code (relating to obscene visual representations of the sexual abuse of children). (3) Offense involving digital forgeries (A) Involving adults Except as provided in subparagraph (C), it shall be unlawful for any person, in interstate or foreign commerce, to use an interactive computer service to knowingly publish a digital forgery of an identifiable individual who is not a minor if\u2014 (i) the digital forgery was published without the consent of the identifiable individual; (ii) what is depicted was not voluntarily exposed by the identifiable individual in a public or commercial setting; (iii) what is depicted is not a matter of public concern; and (iv) publication of the digital forgery\u2014 (I) is intended to cause harm; or (II) causes harm, including psychological, financial, or reputational harm, to the identifiable individual. (B) Involving minors Except as provided in subparagraph (C), it shall be unlawful for any person, in interstate or foreign commerce, to use an interactive computer service to knowingly publish a digital forgery of an identifiable individual who is a minor with intent to\u2014 (i) abuse, humiliate, harass, or degrade the minor; or (ii) arouse or gratify the sexual desire of any person. (C) Exceptions Subparagraphs (A) and (B) shall not apply to\u2014 (i) a lawfully authorized investigative, protective, or intelligence activity of\u2014 (I) a law enforcement agency of the United States, a State, or a political subdivision of a State; or (II) an intelligence agency of the United States; (ii) a disclosure made reasonably and in good faith\u2014 (I) to a law enforcement officer or agency; (II) as part of a document production or filing associated with a legal proceeding; (III) as part of medical education, diagnosis, or treatment or for a legitimate medical, scientific, or education purpose; (IV) in the reporting of unlawful content or unsolicited or unwelcome conduct or in pursuance of a legal, professional, or other lawful obligation; or (V) to seek support or help with respect to the receipt of an unsolicited intimate visual depiction; (iii) a disclosure reasonably intended to assist the identifiable individual; (iv) a person who possesses or publishes a digital forgery of himself or herself engaged in nudity or sexually explicit conduct (as that term is defined in section 2256(2)(A) of title 18, United States Code); or (v) the publication of an intimate visual depiction that constitutes\u2014 (I) child pornography (as that term is defined in section 2256 of title 18, United States Code); or (II) a visual depiction described in subsection (a) or (b) of section 1466A of title 18, United States Code (relating to obscene visual representations of the sexual abuse of children). (4) Penalties (A) Offenses involving adults Any person who violates paragraph (2)(A) or (3)(A) shall be fined under title 18, United States Code, imprisoned not more than 2 years, or both. (B) Offenses involving minors Any person who violates paragraph (2)(B) or (3)(B) shall be fined under title 18, United States Code, imprisoned not more than 3 years, or both. (5) Rules of construction For purposes of paragraphs (2) and (3)\u2014 (A) the fact that the identifiable individual provided consent for the creation of the intimate visual depiction shall not establish that the individual provided consent for the publication of the intimate visual depiction; and (B) the fact that the identifiable individual disclosed the intimate visual depiction to another individual shall not establish that the identifiable individual provided consent for the publication of the intimate visual depiction by the person alleged to have violated paragraph (2) or (3), respectively. (6) Threats (A) Threats involving authentic intimate visual depictions Any person who intentionally threatens to commit an offense under paragraph (2) for the purpose of intimidation, coercion, extortion, or to create mental distress shall be punished as provided in paragraph (4). (B) Threats involving digital forgeries (i) Threats involving adults Any person who intentionally threatens to commit an offense under paragraph (3)(A) for the purpose of intimidation, coercion, extortion, or to create mental distress shall be fined under title 18, United States Code, imprisoned not more than 18 months, or both. (ii) Threats involving minors Any person who intentionally threatens to commit an offense under paragraph (3)(B) for the purpose of intimidation, coercion, extortion, or to create mental distress shall be fined under title 18, United States Code, imprisoned not more than 30 months, or both. (7) Forfeiture (A) In general The court, in imposing a sentence on any person convicted of a violation of paragraph (2) or (3), shall order, in addition to any other sentence imposed and irrespective of any provision of State law, that the person forfeit to the United States\u2014 (i) any material distributed in violation of that paragraph; (ii) the person\u2019s interest in property, real or personal, constituting or derived from any gross proceeds of the violation, or any property traceable to such property, obtained or retained directly or indirectly as a result of the violation; and (iii) any personal property of the person used, or intended to be used, in any manner or part, to commit or to facilitate the commission of the violation. (B) Procedures Section 413 of the Controlled Substances Act ( 21 U.S.C. 853 ), with the exception of subsections (a) and (d), shall apply to the criminal forfeiture of property under subparagraph (A). (8) Restitution The court shall order restitution for an offense under paragraph (2) or (3) in the same manner as under section 2264 of title 18, United States Code. (9) Rule of construction Nothing in this subsection shall be construed to limit the application of any other relevant law, including section 2252 of title 18, United States Code. .\n##### (b) Defenses\nSection 223(e)(1) of the Communications Act of 1934 ( 47 U.S.C. 223(e)(1) ) is amended by striking or (d) and inserting , (d), or (h) .\n##### (c) Technical and conforming amendment\nSubsection (i) of section 223 of the Communications Act of 1934 ( 47 U.S.C. 223 ), as so redesignated by subsection (a), is amended by inserting Definitions .\u2014 before For purposes of this section .\n#### 3. Notice and removal of nonconsensual intimate visual depictions\n##### (a) In general\n**(1) Notice and removal process**\n**(A) Establishment**\nNot later than 1 year after the date of enactment of this Act, a covered platform shall establish a process whereby an identifiable individual (or an authorized person acting on behalf of such individual) may\u2014\n**(i)**\nnotify the covered platform of an intimate visual depiction published on the covered platform that\u2014\n**(I)**\nincludes a depiction of the identifiable individual; and\n**(II)**\nwas published without the consent of the identifiable individual; and\n**(ii)**\nsubmit a request for the covered platform to remove such intimate visual depiction.\n**(B) Requirements**\nA notification and request for removal of an intimate visual depiction submitted under the process established under subparagraph (A) shall include, in writing\u2014\n**(i)**\na physical or electronic signature of the identifiable individual (or an authorized person acting on behalf of such individual);\n**(ii)**\nan identification of, and information reasonably sufficient for the covered platform to locate, the intimate visual depiction of the identifiable individual;\n**(iii)**\na brief statement that the identifiable individual has a good faith belief that any intimate visual depiction identified under clause (ii) is not consensual, including any relevant information for the covered platform to determine the intimate visual depiction was published without the consent of the identifiable individual; and\n**(iv)**\ninformation sufficient to enable the covered platform to contact the identifiable individual (or an authorized person acting on behalf of such individual).\n**(2) Notice of process**\nA covered platform shall provide on the platform a clear and conspicuous notice, which may be provided through a clear and conspicuous link to another web page or disclosure, of the notice and removal process established under paragraph (1)(A) that\u2014\n**(A)**\nis easy to read and in plain language; and\n**(B)**\nprovides information regarding the responsibilities of the covered platform under this section, including a description of how an individual can submit a notification and request for removal.\n**(3) Removal of nonconsensual intimate visual depictions**\nUpon receiving a valid removal request from an identifiable individual (or an authorized person acting on behalf of such individual) using the process described in paragraph (1)(A)(ii), a covered platform shall, as soon as possible, but not later than 48 hours after receiving such request\u2014\n**(A)**\nremove the intimate visual depiction; and\n**(B)**\nmake reasonable efforts to identify and remove any known identical copies of such depiction.\n**(4) Limitation on liability**\nA covered platform shall not be liable for any claim based on the covered platform\u2019s good faith disabling of access to, or removal of, material claimed to be a nonconsensual intimate visual depiction based on facts or circumstances from which the unlawful publishing of an intimate visual depiction is apparent, regardless of whether the intimate visual depiction is ultimately determined to be unlawful or not.\n##### (b) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA failure to reasonably comply with the notice and takedown obligations under subsection (a) shall be treated as a violation of a rule defining an unfair or a deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nExcept as provided in subparagraph (D), the Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Federal Trade Commission under any other provision of law.\n**(D) Scope of jurisdiction**\nNotwithstanding section 4, 5(a)(2), or 6 of the Federal Trade Commission Act ( 15 U.S.C. 44 , 45(a)(2), 46), or any jurisdictional limitation of the Commission, the Commission shall also enforce this section in the same manner provided in subparagraph (A), with respect to organizations that are not organized to carry on business for their own profit or that of their members.\n#### 4. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Consent; digital forgery; identifiable individual; intimate visual depiction**\nThe terms consent , digital forgery , identifiable individual , intimate visual depiction , and minor have the meaning given such terms in section 223(h) of the Communications Act of 1934 ( 47 U.S.C. 223 ), as added by section 2.\n**(3) Covered platform**\n**(A) In general**\nThe term covered platform means a website, online service, online application, or mobile application\u2014\n**(i)**\nthat serves the public; and\n**(ii)**\n**(I)**\nthat primarily provides a forum for user-generated content, including messages, videos, images, games, and audio files; or\n**(II)**\nfor which it is in the regular course of trade or business of the website, online service, online application, or mobile application to publish, curate, host, or make available content of nonconsensual intimate visual depictions.\n**(B) Exclusions**\nThe term covered platform shall not include the following:\n**(i)**\nA provider of broadband internet access service (as described in section 8.1(b) of title 47, Code of Federal Regulations, or successor regulation).\n**(ii)**\nElectronic mail.\n**(iii)**\nExcept as provided in subparagraph (A)(ii)(II), an online service, application, or website\u2014\n**(I)**\nthat consists primarily of content that is not user generated but is preselected by the provider of such online service, application, or website; and\n**(II)**\nfor which any chat, comment, or interactive functionality is incidental to, directly related to, or dependent on the provision of the content described in subclause (I).\n#### 5. Severability\nIf any provision of this Act, or an amendment made by this Act, is determined to be unenforceable or invalid, the remaining provisions of this Act and the amendments made by this Act shall not be affected.",
      "versionDate": "2025-04-28",
      "versionType": "Reported in House"
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
        "actionDate": "2025-05-19",
        "text": "Became Public Law No: 119-12."
      },
      "number": "146",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "TAKE IT DOWN Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-02-24T19:29:50Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2025-02-24T19:29:50Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-02-24T19:29:50Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2025-02-24T19:29:50Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-02-24T19:29:50Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-02-24T19:29:50Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2025-05-20T11:59:20Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-02-24T19:29:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-02-24T18:43:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
    "originChamber": "House",
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
          "measure-id": "id119hr633",
          "measure-number": "633",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-04-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr633v00",
            "update-date": "2025-04-28"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Tools to Address Known Exploitation by Immobilizing Technological Deepfakes On Websites and Networks Act or the TAKE IT DOWN Act</strong></p><p>This bill generally prohibits the nonconsensual online publication of intimate visual depictions of individuals, both authentic and computer-generated, and requires\u00a0certain\u00a0online platforms to promptly remove such depictions upon\u00a0receiving\u00a0notice of their existence.\u00a0</p><p>Specifically, the bill prohibits the online publication of intimate visual depictions of</p><ul><li>an adult subject where publication is intended to cause or does cause harm to the subject, and where the depiction was published without the subject\u2019s consent or, in the case of an authentic depiction, was created or obtained under circumstances where the adult had a reasonable expectation of privacy; or</li><li>a minor subject where publication is intended to abuse or harass the minor or to arouse or gratify the sexual desire of any person.\u00a0</li></ul><p>Violators are subject to mandatory restitution and\u00a0criminal penalties, including prison, a fine, or both. Threats to publish intimate visual depictions of a subject are similarly prohibited under the bill and subject to criminal penalties. \u00a0</p><p>Separately, covered platforms must establish a process through which subjects of intimate visual depictions may notify the platform of the existence of, and request removal of, an intimate visual depiction including the subject that was published without the subject\u2019s consent. Covered platforms must remove such depictions within 48 hours of notification. Under the bill,\u00a0<em>covered platforms</em> are defined as public websites, online services, or applications that primarily provide a forum for user-generated content.</p>"
        },
        "title": "TAKE IT DOWN Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr633.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Tools to Address Known Exploitation by Immobilizing Technological Deepfakes On Websites and Networks Act or the TAKE IT DOWN Act</strong></p><p>This bill generally prohibits the nonconsensual online publication of intimate visual depictions of individuals, both authentic and computer-generated, and requires\u00a0certain\u00a0online platforms to promptly remove such depictions upon\u00a0receiving\u00a0notice of their existence.\u00a0</p><p>Specifically, the bill prohibits the online publication of intimate visual depictions of</p><ul><li>an adult subject where publication is intended to cause or does cause harm to the subject, and where the depiction was published without the subject\u2019s consent or, in the case of an authentic depiction, was created or obtained under circumstances where the adult had a reasonable expectation of privacy; or</li><li>a minor subject where publication is intended to abuse or harass the minor or to arouse or gratify the sexual desire of any person.\u00a0</li></ul><p>Violators are subject to mandatory restitution and\u00a0criminal penalties, including prison, a fine, or both. Threats to publish intimate visual depictions of a subject are similarly prohibited under the bill and subject to criminal penalties. \u00a0</p><p>Separately, covered platforms must establish a process through which subjects of intimate visual depictions may notify the platform of the existence of, and request removal of, an intimate visual depiction including the subject that was published without the subject\u2019s consent. Covered platforms must remove such depictions within 48 hours of notification. Under the bill,\u00a0<em>covered platforms</em> are defined as public websites, online services, or applications that primarily provide a forum for user-generated content.</p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119hr633"
    },
    "title": "TAKE IT DOWN Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Tools to Address Known Exploitation by Immobilizing Technological Deepfakes On Websites and Networks Act or the TAKE IT DOWN Act</strong></p><p>This bill generally prohibits the nonconsensual online publication of intimate visual depictions of individuals, both authentic and computer-generated, and requires\u00a0certain\u00a0online platforms to promptly remove such depictions upon\u00a0receiving\u00a0notice of their existence.\u00a0</p><p>Specifically, the bill prohibits the online publication of intimate visual depictions of</p><ul><li>an adult subject where publication is intended to cause or does cause harm to the subject, and where the depiction was published without the subject\u2019s consent or, in the case of an authentic depiction, was created or obtained under circumstances where the adult had a reasonable expectation of privacy; or</li><li>a minor subject where publication is intended to abuse or harass the minor or to arouse or gratify the sexual desire of any person.\u00a0</li></ul><p>Violators are subject to mandatory restitution and\u00a0criminal penalties, including prison, a fine, or both. Threats to publish intimate visual depictions of a subject are similarly prohibited under the bill and subject to criminal penalties. \u00a0</p><p>Separately, covered platforms must establish a process through which subjects of intimate visual depictions may notify the platform of the existence of, and request removal of, an intimate visual depiction including the subject that was published without the subject\u2019s consent. Covered platforms must remove such depictions within 48 hours of notification. Under the bill,\u00a0<em>covered platforms</em> are defined as public websites, online services, or applications that primarily provide a forum for user-generated content.</p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119hr633"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr633ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr633rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "TAKE IT DOWN Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-04-29T05:53:18Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Tools to Address Known Exploitation by Immobilizing Technological Deepfakes On Websites and Networks Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-04-29T05:53:18Z"
    },
    {
      "title": "TAKE IT DOWN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:07Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TAKE IT DOWN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tools to Address Known Exploitation by Immobilizing Technological Deepfakes On Websites and Networks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require covered platforms to remove nonconsensual intimate visual depictions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:23Z"
    }
  ]
}
```
