# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/682?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/682
- Title: Heartbeat Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 682
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-04-28T08:06:36Z
- Update date including text: 2026-04-28T08:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/682",
    "number": "682",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000376",
        "district": "16",
        "firstName": "Mike",
        "fullName": "Rep. Kelly, Mike [R-PA-16]",
        "lastName": "Kelly",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Heartbeat Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:36Z",
    "updateDateIncludingText": "2026-04-28T08:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
        "item": {
          "date": "2025-01-23T15:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NJ"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TN"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KS"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MI"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KY"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AZ"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "SD"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TN"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "PA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WI"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ID"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KS"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "PA"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MD"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AZ"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "WI"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "SC"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr682ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 682\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Kelly of Pennsylvania (for himself, Mr. Smith of New Jersey , Mr. Aderholt , Mr. Crenshaw , Mrs. Miller of Illinois , Mr. Burchett , Mr. Estes , Mr. Weber of Texas , Mr. Baird , Mr. Moolenaar , Mr. Webster of Florida , Mr. Guthrie , Mr. Hudson , Mr. Ezell , Mr. Allen , Mr. Fallon , Mr. Crane , Mr. Johnson of South Dakota , Mr. Fleischmann , Mr. Bost , Mr. LaHood , Mr. Kelly of Mississippi , Mr. Austin Scott of Georgia , Mr. Feenstra , Mr. Bilirakis , Mr. Thompson of Pennsylvania , Mr. Grothman , Mr. Moore of Alabama , Ms. Tenney , Mr. Fulcher , Mr. Mann , and Mr. Guest ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit abortion in cases where a fetal heartbeat is detectable.\n#### 1. Short title\nThis Act may be cited as the Heartbeat Protection Act of 2025 .\n#### 2. Abortions prohibited without a check for fetal heartbeat, or if a fetal heartbeat is detectable\n##### (a) Abortions prohibited without a check for fetal heartbeat, or if a fetal heartbeat is detectable\nChapter 74 of title 18, United States Code, is amended\u2014\n**(1)**\nin the chapter heading, by striking Partial-Birth ;\n**(2)**\nby inserting after section 1531 the following:\n1532. Abortions prohibited without a check for fetal heartbeat, or if a fetal heartbeat is detectable (a) Offense Any physician who knowingly performs an abortion and thereby kills a human unborn child\u2014 (1) without determining, according to standard medical practice, whether the unborn child has a detectable heartbeat; (2) without informing the mother of the results of that determination; or (3) after determining, according to standard medical practice, that the unborn child has a detectable heartbeat, shall be fined under this title or imprisoned not more than 5 years, or both. This subsection does not apply to an abortion that is necessary to save the life of a mother whose life is endangered by a physical disorder, physical illness, or physical injury, including a life-endangering physical condition caused by or arising from the pregnancy itself, but not including psychological or emotional conditions. (b) Exceptions Subsection (a) shall not apply if\u2014 (1) in reasonable medical judgment, the abortion is necessary to save the life of a pregnant woman whose life is endangered by a physical disorder, physical illness, or physical injury, including a life-endangering physical condition caused by or arising from the pregnancy itself, but not including psychological or emotional conditions; (2) the pregnancy is the result of rape against an adult woman, and at least 48 hours prior to the abortion\u2014 (A) she has obtained counseling for the rape; or (B) she has obtained medical treatment for the rape or an injury related to the rape; or (3) the pregnancy is a result of rape against a minor or incest against a minor, and the rape or incest has been reported at any time prior to the abortion to either\u2014 (A) a government agency legally authorized to act on reports of child abuse; or (B) a law enforcement agency. (c) Documentation requirements (1) Documentation pertaining to adults A physician who performs or attempts to perform an abortion under an exception provided by subsection (b)(2) shall, prior to performing the abortion, place in the patient medical file documentation from a hospital licensed by the State or operated under authority of a Federal agency, a medical clinic licensed by the State or operated under authority of a Federal agency, from a personal physician licensed by the State, a counselor licensed by the State, or a victim\u2019s rights advocate provided by a law enforcement agency that the adult woman seeking the abortion obtained medical treatment or counseling for the rape or an injury related to the rape. (2) Documentation pertaining to minors A physician who performs or attempts to perform an abortion under an exception provided by subsection (b)(3) shall, prior to performing the abortion, place in the patient medical file documentation from a government agency legally authorized to act on reports of child abuse that the rape or incest was reported prior to the abortion; or, as an alternative, documentation from a law enforcement agency that the rape or incest was reported prior to the abortion. (d) Requirement for data retention Paragraph (j)(2) of section 164.530 of title 45, Code of Federal Regulations, shall apply to documentation required to be placed in a patient\u2019s medical file pursuant to paragraph (6) of such section and a consent form required to be retained in a patient\u2019s medical file pursuant to paragraph (7) of such section in the same manner and to the same extent as such paragraph applies to documentation required by paragraph (j)(1) of such section. (e) Additional exceptions and requirements (1) Exclusion of certain facilities Notwithstanding the definitions set forth in subsection (j), the counseling described in subsection (b)(2)(A) and subsection (c)(1) or medical treatment may not be provided by a facility that performs abortions (unless that facility is a hospital). (2) Rule of construction in cases of reports to law enforcement The requirements of subsection (b)(2) do not apply if the rape has been reported at any time prior to the abortion to a law enforcement agency or Department of Defense victim assistance personnel. (f) Defendant may seek hearing A defendant indicted for an offense under this section may seek a hearing before the State Medical Board on whether the physician's conduct was necessary to save the life of the mother whose life was endangered by a physical disorder, physical illness, or physical injury, including a life-endangering physical condition caused by or arising from the pregnancy itself, but not including psychological or emotional conditions. The findings on that issue are admissible on that issue at the trial of the defendant. Upon a motion of the defendant, the court shall delay the beginning of the trial for not more than 30 days to permit such a hearing to take place. (g) No liability for the mother on whom abortion is performed A mother upon whom an abortion is performed may not be prosecuted under this section, for a conspiracy to violate this section, or for an offense under section 2, 3, or 4 of this title based on a violation of this section. (h) Requirement for data retention The physician shall include in the medical file of the mother documentation of the determination, according to standard medical practice, of whether the unborn child has a detectable heartbeat, the results of that determination, notification of the mother of those results, and any information entered into evidence in any proceedings under subsection (b). Paragraph (j)(2) of section 164.530 of title 45, Code of Federal Regulations, shall apply to such documentation. (i) Severability If any provision of this section or the application of such provision to any person or circumstance is held to be invalid, the remainder of this section and the application of the provisions of the remainder to any person or circumstance shall not be affected thereby. (j) Definitions In this section: (1) The term counseling means counseling provided by a counselor licensed by the State, or a victims rights advocate provided by a law enforcement agency. (2) The term medical treatment means treatment provided at a hospital licensed by the State or operated under authority of a Federal agency, at a medical clinic licensed by the State or operated under authority of a Federal agency, or from a personal physician licensed by the State. (3) The term abortion means the use or prescription of any instrument, medicine, drug, or any other substance or device\u2014 (A) to intentionally kill the unborn child of a woman known to be pregnant; or (B) to intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) after viability to produce a live birth and preserve the life and health of the child born alive; or (ii) to remove a dead unborn child. (4) The term attempt , with respect to an abortion, means conduct that, under the circumstances as the actor believes them to be, constitutes a substantial step in a course of conduct planned to culminate in performing an abortion. (5) The term facility means any medical or counseling group, center or clinic and includes the entire legal entity, including any entity that controls, is controlled by, or is under common control with such facility. (6) The term perform , with respect to an abortion, includes inducing an abortion through a medical or chemical intervention including writing a prescription for a drug or device intended to result in an abortion. (7) The term physician means a person licensed to practice medicine and surgery or osteopathic medicine and surgery, or otherwise legally authorized to perform an abortion. (8) The term reasonable medical judgment means a medical judgment that would be made by a reasonably prudent physician, knowledgeable about the case and the treatment possibilities with respect to the medical conditions involved. (9) The term unborn child means an individual organism of the species homo sapiens, beginning at fertilization, until the point of being born alive as defined in section 8(b) of title 1. (10) The term woman means a female human being whether or not she has reached the age of majority. (k) Rules of construction (1) Greater protections Nothing in this section may be construed to pre-empt or limit any Federal, State, or local law that provides greater protections for an unborn child than those provided in this section. (2) Creation of recognition of right Nothing in this section may be construed to create or recognize a right to abortion or to make lawful an abortion that is unlawful on the effective date of this section. ; and\n**(3)**\nin the table of sections, by inserting after the item pertaining to section 1841 the following:\n1532. Abortions prohibited without a check for fetal heartbeat, or if a fetal heartbeat is detectable. .\n##### (b) Clerical amendment\nThe table of chapters for part I of title 18, United States Code, is amended, in the item relating to chapter 74, to read as follows:\n74. Abortions 1531 .",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in House"
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
            "name": "Abortion",
            "updateDate": "2025-03-19T16:00:55Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-03-19T16:00:55Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-19T16:00:55Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-03-19T16:00:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-24T12:20:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr682",
          "measure-number": "682",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-05-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr682v00",
            "update-date": "2025-05-05"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Heartbeat Protection Act of 2025</strong></p><p>This bill makes it a crime for a physician to knowingly perform an abortion (1) without determining whether the unborn child has a detectable heartbeat, (2) without informing the mother of the results, or (3) after determining that an unborn child has a detectable heartbeat.</p><p>A physician who performs a prohibited abortion is subject to criminal penalties\u2014a fine, up to five years in prison, or both.</p><p>The bill provides an exception for an abortion that is necessary to save the life of a mother whose life is endangered by a physical (but not psychological or emotional) disorder, illness, or condition. It also provides exceptions for certain pregnancies that are the result of rape or incest. A physician who performs or attempts to perform an abortion under an exception must comply with specified requirements.</p><p>A woman who undergoes a prohibited abortion may not be prosecuted for violating or conspiring to violate the provisions of this bill.</p>"
        },
        "title": "Heartbeat Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr682.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Heartbeat Protection Act of 2025</strong></p><p>This bill makes it a crime for a physician to knowingly perform an abortion (1) without determining whether the unborn child has a detectable heartbeat, (2) without informing the mother of the results, or (3) after determining that an unborn child has a detectable heartbeat.</p><p>A physician who performs a prohibited abortion is subject to criminal penalties\u2014a fine, up to five years in prison, or both.</p><p>The bill provides an exception for an abortion that is necessary to save the life of a mother whose life is endangered by a physical (but not psychological or emotional) disorder, illness, or condition. It also provides exceptions for certain pregnancies that are the result of rape or incest. A physician who performs or attempts to perform an abortion under an exception must comply with specified requirements.</p><p>A woman who undergoes a prohibited abortion may not be prosecuted for violating or conspiring to violate the provisions of this bill.</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119hr682"
    },
    "title": "Heartbeat Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Heartbeat Protection Act of 2025</strong></p><p>This bill makes it a crime for a physician to knowingly perform an abortion (1) without determining whether the unborn child has a detectable heartbeat, (2) without informing the mother of the results, or (3) after determining that an unborn child has a detectable heartbeat.</p><p>A physician who performs a prohibited abortion is subject to criminal penalties\u2014a fine, up to five years in prison, or both.</p><p>The bill provides an exception for an abortion that is necessary to save the life of a mother whose life is endangered by a physical (but not psychological or emotional) disorder, illness, or condition. It also provides exceptions for certain pregnancies that are the result of rape or incest. A physician who performs or attempts to perform an abortion under an exception must comply with specified requirements.</p><p>A woman who undergoes a prohibited abortion may not be prosecuted for violating or conspiring to violate the provisions of this bill.</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119hr682"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr682ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Heartbeat Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T11:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Heartbeat Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T11:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit abortion in cases where a fetal heartbeat is detectable.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T11:48:32Z"
    }
  ]
}
```
