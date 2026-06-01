# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2797?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2797
- Title: House Expansion Commission Act
- Congress: 119
- Bill type: HR
- Bill number: 2797
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2026-03-06T09:07:21Z
- Update date including text: 2026-03-06T09:07:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2797",
    "number": "2797",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "House Expansion Commission Act",
    "type": "HR",
    "updateDate": "2026-03-06T09:07:21Z",
    "updateDateIncludingText": "2026-03-06T09:07:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:02:15Z",
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
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2797ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2797\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Ms. Stevens introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish a commission to study and develop proposals for expanding the House of Representatives, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the House Expansion Commission Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nFor nearly a century, the number of members of the House of Representatives has been set at the 1929 cap of 435 members.\n**(2)**\nThe number of constituents represented by each member of the House of Representatives has dramatically increased since the number of members of the House of Representatives was arbitrarily capped in 1929.\n**(3)**\nThe 1929 cap on the number of members of the House of Representatives was instituted when the United States population was 123 million. Since then, the United States population has tripled to about 346 million which means the average congressional district now represents nearly 800,000 constituents, according to data from the Bureau of the Census.\n**(4)**\nWith current population growth estimates, the average congressional district could have approximately 829,000 constituents by 2050.\n**(5)**\nA growing movement in Congress, and in think tanks, seeks to increase the number of members of the House of Representatives to increase public access to members, improve diversity, and enhance Member ability to serve their constituents.\n**(6)**\nRepresentative Earl Blumenauer (D-Ore.) introduced House bill 622, the Restoring Equal and Accountable Legislators in the House Act, in the One Hundred Eighteenth Congress, which would add 150 seats to the House of Representatives, increasing it to 585 members.\n#### 3. Establishment\nThere is established a commission to be known as the U.S. House of Representatives Expansion Commission (in this Act referred to as the Commission ).\n#### 4. Duties of commission\n##### (a) Study\nThe Commission shall study\u2014\n**(1)**\nthe current size of the membership of the House of Representatives considering\u2014\n**(A)**\nthe correlation between the current size of the House and fair representation and efficacy; and\n**(B)**\nwhether an expanded House of Representatives can better serve Congress\u2019 core Article 1 function;\n**(2)**\nthe option of a one-time expansion compared to the feasibility of recurring expansions;\n**(3)**\nthe so called Cube Root Law , Wyoming Rule , and other relevant methods to increase the size of the House of Representatives;\n**(4)**\nthe cost implications and practical challenges to the House of Representatives associated with expanding the number of members of the House of Representatives including the logistics for\u2014\n**(A)**\noffices and meeting spaces;\n**(B)**\ncongressional support entities;\n**(C)**\nhiring congressional staff;\n**(D)**\nvoting by members of the House of Representatives;\n**(E)**\nHouse administration offices; and\n**(F)**\nfunding;\n**(5)**\nhow countries with similar legislative structures expanded their legislative bodies and the outcomes of such expansions;\n**(6)**\nthe historical context of the last time the number of members of the House of Representatives was changed and key motivations behind the amendments made by the Act entitled An Act to provide for the fifteenth and subsequent decennial census and to provide for apportionment of Representatives in Congress , approved June 18, 1929 ( 2 U.S.C. 2a );\n**(7)**\nwhether an expanded House of Representatives can better exercise the powers vested in Article I of the Constitution;\n**(8)**\nhow expanding the number of members of the House of Representatives may affect district size variance across States and impact underrepresented constituencies; and\n**(9)**\nthe potential effects of an expanded House of Representative on the ability of the House to enact laws.\n##### (b) Consultation\nIn conducting the study under subsection (a), the Commission shall consult with the Architect of the Capitol, the Administrator of General Services, the Sergeant at Arms of the House of Representatives, the Chief Administrative Officer of the House of Representatives, the Clerk of the House of Representatives, and such other persons as the Commission considers appropriate.\n##### (c) Report and proposals\nNot later than 2 years after the first meeting of the Commission, the Commission shall submit to the President and to the Congress a report of the study of the Commission, and shall include in the report proposals based on such study for\u2014\n**(1)**\nexpanding the size of the membership of the House of Representatives;\n**(2)**\npotential ways to expand the House of Representatives to bolster the key role of the House of Representatives in representing the American people in Congress; and\n**(3)**\nsolutions to any identified challenges that may arise from such expansion.\n#### 5. Membership\n##### (a) Number and appointment\nThe Commission shall be composed of 13 members who are not Members of Congress at the time of appointment, and who shall be appointed not later than 90 days after the date of the enactment of this Act, as follows:\n**(1)**\n5 members appointed by the Speaker of the House of Representatives.\n**(2)**\n5 members appointed by the minority leader of the House of Representatives.\n**(3)**\n1 individual, appointed by the majority leader of the Senate, who previously served in the House of Representatives.\n**(4)**\n1 individual, appointed by the minority leader of the Senate, who previously served in the House of Representatives.\n**(5)**\n1 member appointed by the Speaker of the House of Representatives and the minority leader of the House of Representatives to serve as Chairperson of the Commission.\n##### (b) Terms\n**(1) In general**\nEach member shall be appointed for the life of the Commission.\n**(2) Vacancies**\nA vacancy in the Commission shall be filled in the manner in which the original appointment was made.\n**(3) Priority**\nIn making appointments under this section, the appointing authorities shall seek to appoint individuals who are particularly qualified to perform the functions of the Commission, by reason of either practical experience or academic expertise in politics, government, mathematics, or statistics.\n##### (c) Basic pay\n**(1) Rates of pay**\nExcept as provided in paragraph (2), Members shall serve without pay.\n**(2) Travel expenses**\nEach member shall receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code.\n##### (d) Quorum\n7 members of the Commission shall constitute a quorum, but a lesser number may hold hearings.\n##### (e) Meetings\nThe Commission shall meet at the call of the Chairperson or a majority of its members.\n#### 6. Personnel of Commission\n##### (a) Director\nThe Commission shall have a Director who shall be appointed by a majority vote of the Commission. To the extent or in the amounts provided in advance in appropriation Acts, the Director shall be paid at a rate not to exceed the rate of basic pay for level IV of the Executive Schedule.\n##### (b) Staff\nThe Director, with the approval of the Commission, and the Commission may appoint such personnel as may be necessary to enable the Commission to carry out its duties, without regard to the provisions of title 5, United States Code, governing appointments in the competitive service, and without regard to the provisions of chapter 51 and subchapter III of chapter 53 of such title relating to classification and General Schedule pay rates, except that no rate of pay fixed under this subsection may exceed\u2014\n**(1)**\nthe equivalent of that payable to a person occupying a position at level IV of the Executive Schedule, in the case of an employee appointed by the Director; and\n**(2)**\nthe equivalent of that payable to a person occupying a position at level V of the Executive Schedule, in the case of an employee appointed by the Commission.\n##### (c) Experts and consultants\nWith the approval of the Commission, the Director may procure temporary and intermittent services under section 3109(b) of title 5, United States Code.\n##### (d) Detail of government employees\nUpon the request of the Commission, the head of any Federal agency may detail, without reimbursement, any of the personnel of such agency to the Commission to assist in carrying out the duties of the Commission. Any such detail shall not interrupt or otherwise affect the civil service status or privileges of the personnel.\n#### 7. Powers of Commission\n##### (a) Hearings and sessions\nThe Commission may, for the purpose of carrying out this Act, hold hearings, sit and act at times and places, take testimony, and receive evidence as the Commission considers appropriate.\n##### (b) Powers of members and groups of members\nAny member or group of members may, if authorized by the Commission, take any action which the Commission is authorized to take by this section.\n##### (c) Obtaining official data\nThe Commission may secure directly from any Federal agency information necessary to enable it to carry out its duties, if the information may be disclosed under section 552 of title 5, United States Code. Upon request of the Chairperson of the Commission, the head of such agency shall furnish such information to the Commission.\n##### (d) Administrative support services\nUpon the request of the Commission, the Administrator of General Services shall provide to the Commission, on a reimbursable basis, the administrative support services necessary for the Commission to carry out its responsibilities under this Act.\n##### (e) Volunteer services\nNotwithstanding 1342 of title 31, United States Code, the Commission may accept and use voluntary and uncompensated services as the Commission determines necessary.\n##### (f) Postal service\nThe Commission may use the United States mails in the same manner and under the same conditions as departments and agencies of the United States.\n##### (g) Contract authority\nThe Commission may enter into contracts for the acquisition of administrative supplies and equipment for use by the Commission, to the extent that funds are available for such purpose.\n#### 8. Termination\nThe Commission shall terminate 90 days after submitting the report under section 4(c).\n#### 9. Authorization of appropriations\nThere is authorized to be appropriated such sums as may be necessary to carry out this Act.",
      "versionDate": "2025-04-09",
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
        "name": "Congress",
        "updateDate": "2025-05-08T18:02:27Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2797ih.xml"
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
      "title": "House Expansion Commission Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "House Expansion Commission Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a commission to study and develop proposals for expanding the House of Representatives, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T06:18:32Z"
    }
  ]
}
```
