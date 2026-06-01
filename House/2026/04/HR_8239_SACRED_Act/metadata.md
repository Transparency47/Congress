# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8239?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8239
- Title: SACRED Act
- Congress: 119
- Bill type: HR
- Bill number: 8239
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-05-30T08:06:08Z
- Update date including text: 2026-05-30T08:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8239",
    "number": "8239",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001201",
        "district": "3",
        "firstName": "Thomas",
        "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
        "lastName": "Suozzi",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "SACRED Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:08Z",
    "updateDateIncludingText": "2026-05-30T08:06:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
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
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
          "date": "2026-04-09T15:32:05Z",
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
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "OH"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NJ"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "FL"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "IL"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "TX"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "OH"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8239ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8239\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Suozzi (for himself and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit harassment of persons lawfully exercising or seeking to exercise the First Amendment right of religious freedom at a place of religious worship, within a distance of 100 feet or closer to such place of religious worship, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Access to Congregations and Religious Establishments from Disruption Act or the SACRED Act .\n#### 2. Freedom of access to places of religious worship\n##### (a) In general\nChapter 13 of title 18, United States Code, is amended by adding at the end the following:\n251. Freedom of access to places of religious worship (a) Prohibited activities Whoever, in or affecting interstate or foreign commerce\u2014 (1) engages in any course of conduct within 100 feet of a place of religious worship, with the intent to intimidate or obstruct the passage of any person exercising or seeking to exercise the First Amendment right to religious freedom therein, and in a manner that causes any person to reasonably fear for their physical safety while entering or exiting the place of religious worship; or (2) within 100 feet of a place of religious worship, intentionally approaches and harasses any person seeking to exercise the First Amendment right to religious freedom, within 8 feet of such person, shall be punished as provided in subsection (b). (b) Penalties Whoever violates this section shall\u2014 (1) in the case of a first offense, be fined in accordance with this title, or imprisoned not more than one year, or both; and (2) in the case of a second or subsequent offense after a prior conviction under this section, be fined in accordance with this title, or imprisoned not more than 3 years, or both; except that for an offense involving exclusively nonviolent conduct, the fine shall be not more than $10,000 and the length of imprisonment shall be not more than six months, or both, for the first offense; and the fine shall, notwithstanding section 3571, be not more than $25,000 and the length of imprisonment shall be not more than 18 months, or both, for a subsequent offense; and except that if bodily injury results, the length of imprisonment shall be not more than 10 years, and if death results, it shall be for any term of years or for life. (c) Civil remedies (1) Right of action (A) In general Any person aggrieved by reason of the conduct prohibited by subsection (a) may commence a civil action for the relief set forth in subparagraph (B), except that such an action may be brought only by a person lawfully exercising or seeking to exercise the First Amendment right of religious freedom at a place of religious worship or by the entity that owns or operates such place of religious worship. (B) Relief In any action under subparagraph (A), the court may award appropriate relief, including temporary, preliminary or permanent injunctive relief and compensatory and punitive damages, as well as the costs of suit and reasonable fees for attorneys and expert witnesses. With respect to compensatory damages, the plaintiff may elect, at any time prior to the rendering of final judgment, to recover, in lieu of actual damages, an award of statutory damages in the amount of $5,000 per violation. (2) Action by attorney general of the united states (A) In general If the Attorney General of the United States has reasonable cause to believe that any person or group of persons is being, has been, or may be injured by conduct constituting a violation of this section, the Attorney General may commence a civil action in any appropriate United States District Court. (B) Relief In any action under subparagraph (A), the court may award appropriate relief, including temporary, preliminary or permanent injunctive relief, and compensatory damages to persons aggrieved as described in paragraph (1)(B). The court, to vindicate the public interest, may also assess a civil penalty against each respondent\u2014 (i) in an amount not exceeding $10,000 for a nonviolent offense and $15,000 for other first violations; and (ii) in an amount not exceeding $15,000 for a nonviolent offense and $25,000 for any other subsequent violation. (3) Actions by state attorneys general (A) In general If the Attorney General of a State has reasonable cause to believe that any person or group of persons is being, has been, or may be injured by conduct constituting a violation of this section, such Attorney General may commence a civil action in the name of such State, as parens patriae on behalf of natural persons residing in such State, in any appropriate United States District Court. (B) Relief In any action under subparagraph (A), the court may award appropriate relief, including temporary, preliminary or permanent injunctive relief, compensatory damages, and civil penalties as described in paragraph (2)(B). (d) Rules of construction Nothing in this section shall be construed\u2014 (1) to prohibit any expressive conduct (including peaceful picketing or other peaceful demonstration) occurring outside places of religious worship protected from legal prohibition by the First Amendment to the Constitution; or (2) to provide exclusive criminal penalties or civil remedies with respect to the conduct prohibited by this section, or to preempt State or local laws that may provide such penalties or remedies. (e) Definitions For purposes of this section: (1) The term obstruct means to render impassable ingress to or egress from a place of religious worship, or to render passage to or from a place of religious worship unreasonably difficult or hazardous. (2) The term intimidate means to place a person in reasonable apprehension of imminent physical injury to himself or herself or to another person. (3) The term harass means to commit a serious act or engage in a course of conduct directed at a specific person that interferes with their freedom of movement, and is intended to and does place that person in reasonable fear of physical harm, or is intended to and does cause that person to reasonably experience substantial emotional distress. (4) The term course of conduct means a series of acts over a period of time, however short, indicating a continuity of purpose. (5) The term serious act means a single act of threatening, intimidating, or violent conduct. (6) The term place of religious worship means any building, structure or space that is used primarily for religious worship activities or to provide religious education or instruction, and includes the parking lot, parking lot entrance, driveway and driveway entrance of any such building, structure, or space. .\n##### (b) Clerical amendment\nThe table of sections for chapter 13 of title 18, United States Code, is amended by adding at the end the following:\n251. Freedom of access to places of religious worship. .",
      "versionDate": "2026-04-09",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-17T18:52:58Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8239ih.xml"
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
      "title": "SACRED Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T09:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SACRED Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T09:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Access to Congregations and Religious Establishments from Disruption Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T09:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit harassment of persons lawfully exercising or seeking to exercise the First Amendment right of religious freedom at a place of religious worship, within a distance of 100 feet or closer to such place of religious worship, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T09:18:55Z"
    }
  ]
}
```
