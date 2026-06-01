# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/543?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/543
- Title: Fair Play for Women Act
- Congress: 119
- Bill type: S
- Bill number: 543
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2025-12-05T21:51:55Z
- Update date including text: 2025-12-05T21:51:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/543",
    "number": "543",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Fair Play for Women Act",
    "type": "S",
    "updateDate": "2025-12-05T21:51:55Z",
    "updateDateIncludingText": "2025-12-05T21:51:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T19:14:36Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "OR"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "WI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s543is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 543\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Murphy (for himself, Mr. Blumenthal , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit certain discrimination against athletes on the basis of sex by State athletic associations, intercollegiate athletic associations, and covered institutions of higher education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Play for Women Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMore than 50 years ago, Congress passed title IX of the Education Amendments of 1972 (referred to in this section as title IX ), helping to transform participation in and support for women\u2019s sports by barring discrimination on the basis of sex in all schools that receive Federal funding, including in their athletic programs.\n**(2)**\nSince the passage of title IX, millions more women and girls have had the opportunity to compete in school-based athletics. In high school athletics, athletic participation opportunities have increased from nearly 300,000 in 1972 to more than 3,400,000 in 2019. In intercollegiate athletics, opportunities have increased from nearly 30,000 in 1972 to 215,000 in 2020 on teams sponsored by institutions who are members of the National Collegiate Athletic Association (referred to in this section as the NCAA ).\n**(3)**\nDespite progress, women and girls still face unequal opportunities and unfair treatment in school-based athletics. In high school athletics, girls have over 1,000,000 fewer athletic opportunities than boys, with schools providing girls with 43 percent of all athletic opportunities while girls represent nearly half of all students. In intercollegiate athletics, colleges would need to provide women with an additional 148,000 sports opportunities to match the same ratio of sports opportunities per student as is offered to men. Overall, girls still do not have the participation opportunities provided to boys before the enactment of title IX, over 50 years ago.\n**(4)**\nGirls of color are often most impacted by unequal resources and unfair treatment. At high schools predominantly attended by white students, girls have 82 percent of the opportunities that boys have to play sports, while at high schools predominantly attended by students of color, girls have only 67 percent of the opportunities that boys have to play sports.\n**(5)**\nAs part of title IX athletics requirements, schools can show they are compliant by providing athletic participation opportunities for men and women that are substantially proportionate to their respective enrollment rates. Yet, a Government Accountability Office report from 2024 found that 93 percent of all colleges had athletic participation rates for women that were lower than their enrollment rate at the colleges. At 63 percent of colleges, women\u2019s athletic participation rates were at least 10 percentage points lower than their enrollment rates. Overall, the athletic participation rate for collegiate women was 14 percent less than their enrollment rate. Despite widespread noncompliance with title IX athletics requirements, no college has ever had Federal funding rescinded nor been sued by the Federal government for noncompliance.\n**(6)**\nThe magnitude of current gaps in intercollegiate athletics participation opportunities is likely undercounted, as investigations of intercollegiate athletics data have found that the majority of NCAA member institutions inflate the number of women participating in sports by double- and triple-counting women athletes who participate in more than one sport more often than the institutions double- and triple-count their counterparts who are men, counting men who are practice players on women\u2019s teams as women athletes, and packing women\u2019s teams with extra players who never end up competing.\n**(7)**\nWomen and girls in sports also face unfair treatment. They are frequently provided worse facilities, equipment, and uniforms than men and boys, and they receive less financial support and publicity from their schools. In the 2019\u20132020 academic year, women received $252,000,000 less than men in athletic-based scholarships, and for every dollar colleges spent on recruiting, travel, and equipment for men\u2019s sports, they spent 58 cents, 62 cents, and 73 cents, respectively, for women\u2019s sports.\n**(8)**\nAmid ongoing unfair treatment, athletes and athletics-related staff too often are unaware of the rights and obligations provided by title IX. In surveys of children and their parents, the majority report not knowing what title IX is. A study conducted by the Government Accountability Office in 2017 found that most high school athletic administrators were unaware of who their title IX coordinator was or felt unsupported by their title IX coordinator. In intercollegiate athletics, most coaches report that they never received formal training about title IX as part of the preparation for their jobs.\n#### 3. Purposes\nThe purposes of this Act are to\u2014\n**(1)**\naddress unfair and discriminatory treatment of women and girls in sports in elementary and secondary schools, as well as institutions of higher education;\n**(2)**\nimprove the collection and transparency of data pertaining to participation in and support for women\u2019s and girls\u2019 sports at schools receiving Federal financial assistance;\n**(3)**\nensure all students participating in athletics, as well as those who work in school-sponsored athletics, are aware of and understand the nondiscrimination rights of students related to their athletic opportunities; and\n**(4)**\nensure all students have equal access to high-quality and supportive athletic opportunities.\n#### 4. Definitions\nIn this Act:\n**(1) ESEA terms**\nThe terms elementary school and secondary school have the meanings given those terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Collegiate**\nThe term collegiate , used with respect to athletics, means intramural and club-level athletics or other athletics, in which all participants attend the same covered institution of higher education.\n**(3) Covered institution of higher education**\nThe term covered institution of higher education means an entity that is described in section 908(2)(A) of the Education Amendments of 1972 ( 20 U.S.C. 1687(2)(A) ) and covered by section 908 of those Amendments ( 20 U.S.C. 1687 ).\n**(4) Covered local educational agency**\nThe term covered local educational agency means such an agency that is described in section 908(2)(B) of the Education Amendments of 1972 ( 20 U.S.C. 1687(2)(B) ) and covered by section 908 of those Amendments.\n**(5) Intercollegiate athletic association**\nThe term intercollegiate athletic association means any conference, association, or other group or organization, established by or comprised of 2 or more covered institutions of higher education, that\u2014\n**(A)**\ngoverns competitions among, or otherwise exercises authority over intercollegiate athletics at, such institutions of higher education who are members of or under the authority of the intercollegiate athletic association; and\n**(B)**\nis engaged in commerce or an industry or activity affecting commerce.\n**(6) State athletic association**\nThe term State athletic association means any association, organization, or other group, established by or comprised of 2 or more elementary schools or secondary schools that receive Federal funding, that governs competition among or otherwise exercises authority over elementary school, secondary school, or interscholastic athletics, at such federally funded elementary schools or secondary schools.\n**(7) Title IX coordinator**\nThe term title IX coordinator means the individual who coordinates the efforts of a covered school system to comply with and carry out the responsibilities of the covered local educational agency under title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ).\n#### 5. Discrimination by State and intercollegiate athletic associations, local educational agencies, and covered institutions of higher education\n##### (a) Elementary or Secondary School\nNo State athletic association or covered local educational agency shall, on the basis of sex, subject any athlete to discrimination with respect to elementary school, secondary school, or interscholastic athletics, including discrimination through\u2014\n**(1)**\nthe rules it sets for elementary school, secondary school, or interscholastic athletics;\n**(2)**\nthe sports\u2014\n**(A)**\nrequired for membership in a State athletic association;\n**(B)**\ncompetitions sponsored by the State athletic association or covered local educational agency, respectively; or\n**(C)**\nchampionships sponsored by that association or agency; or\n**(3)**\nthe location, facilities, or amenities provided for competitions or championships sponsored by that association or agency.\n##### (b) Higher education\n**(1) In general**\nNo intercollegiate athletic association or covered institution of higher education shall, on the basis of sex, subject any athlete to discrimination with respect to intercollegiate or (subject to paragraph (2)) collegiate athletics, including discrimination through\u2014\n**(A)**\nthe rules it sets for intercollegiate athletics or collegiate athletics;\n**(B)**\nthe sports\u2014\n**(i)**\nrequired for membership in an intercollegiate athletic association, or required for participation in collegiate athletics at a covered institution of higher education;\n**(ii)**\ncompetitions sponsored by the intercollegiate athletic association, or collegiate athletic competitions sponsored by the covered institution of higher education; or\n**(iii)**\nchampionships sponsored by the intercollegiate athletic association, or collegiate athletic championships sponsored by the covered institution of higher education;\n**(C)**\nthe location, facilities, or amenities provided for competitions or championships sponsored by the intercollegiate athletic association, or for collegiate athletic competitions or championships sponsored by the institution;\n**(D)**\nthe provision or arrangement for the provision of goods or services (including benefits) for competitions or championships sponsored by the intercollegiate athletic association, or for collegiate athletic competitions or championships sponsored by such an institution; or\n**(E)**\nthe distribution of revenues or other benefits to members of or such institutions under the authority of the intercollegiate athletic association, or to teams, clubs, or other entities participating in collegiate athletics at the institution.\n**(2) Limitation**\nOnly a covered institution of higher education may be considered to have committed a violation of paragraph (1) with respect to collegiate athletics.\n##### (c) Private right of action\n**(1) In general**\nAn individual who seeks to participate, participates, or previously participated in athletics covered under subsection (a) or (b), offered under the authority of an intercollegiate athletic association or State athletic association, or by a covered institution of higher education or covered local educational agency, may bring an action in any Federal or State court of competent jurisdiction against the athletic association, institution, or agency involved, alleging a violation of this section.\n**(2) Relief**\nThe court may award all legal or equitable relief that may be appropriate for such a violation. The legal relief may include compensatory damages for all injuries, including financial injuries, unequal treatment, emotional distress, humiliation, and pain and suffering, as well as punitive damages, attorney\u2019s fees, and expert fees.\n##### (d) Training\n**(1) Associations**\nEach State athletic association or intercollegiate athletic association shall ensure that each employee of the State athletic association or intercollegiate athletic association receives, at least once per year, training on the provisions of this section, including the rights delineated under this section and the procedures for bringing actions under this section.\n**(2) Covered institutions of higher education**\nEach covered institution of higher education shall ensure that each employee of the institution with an employment function relating to collegiate athletics receives, at least once per year, such training.\n**(3) Covered local educational agency**\nEach covered local educational agency shall ensure that each employee of the local educational agency with an employment function relating to athletics receives, at least once per year, such training.\n#### 6. Expanding athletics disclosure requirements\n##### (a) Institutions of higher education\nSection 485(g) of the Higher Education Act of 1965 ( 20 U.S.C. 1092(g) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A)\u2014\n**(i)**\nby inserting collegiate (including intramural and club-level) or before intercollegiate athletic program ; and\n**(ii)**\nby inserting collegiate and before intercollegiate athletics ;\n**(B)**\nin subparagraph (B), by striking clause (i) and inserting the following:\n(i) The total number of participants, by team. ;\n**(C)**\nin subparagraph (C)\u2014\n**(i)**\nby striking The total amount and inserting the following: (i) The total amount ; and\n**(ii)**\nby adding at the end the following:\n(ii) For each men\u2019s and women\u2019s intercollegiate sport\u2014 (I) the total amount of athletically related student aid; (II) the total number of athletically related scholarships, and the average amount of such scholarships; (III) the total number of athletically related scholarships that fund the full cost of tuition at the institution; (IV) the total number of athletically related scholarships that fund the full cost of attendance for the athlete; (V) the total number of athletically related scholarships awarded for a period equal to or less than one year; and (VI) the total number of athletically related scholarships awarded for a period equal to or greater than 4 academic years. ;\n**(D)**\nin subparagraph (E), by inserting and disaggregated by each men\u2019s sport and each women\u2019s sport before the period at the end;\n**(E)**\nin subparagraph (G), by inserting (which, for purposes of this subparagraph, includes compensation, bonuses, benefits, and buyouts paid to coaches and reportable by the institution or related entities, including booster clubs and foundations) before of the head coaches of men's teams ;\n**(F)**\nin subparagraph (H), by inserting (which, for purposes of this subparagraph, includes compensation, bonuses, benefits, and buyouts paid to coaches and reportable by the institution or related entities, including booster clubs and foundations) before of the assistant coaches of men's teams ;\n**(G)**\nin subparagraph (I)\u2014\n**(i)**\nby striking clause (i) and inserting the following:\n(i) The revenues from the institution\u2019s intercollegiate athletics activities, in the aggregate and disaggregated by each men\u2019s sport and each women\u2019s sport, including\u2014 (I) total revenues; and (II) each category of revenues described in clause (ii). ; and\n**(ii)**\nin clause (ii)\u2014\n**(I)**\nby inserting collegiate and before intercollegiate ; and\n**(II)**\nby striking , and advertising, but revenues and all that follows through the period at the end and inserting , advertising, and, to the extent practicable, student activities fees and alumni contributions. ;\n**(H)**\nby striking clause (i) of subparagraph (J) and inserting the following:\n(i) The expenses made by the institution for the institution\u2019s intercollegiate athletics activities, in the aggregate and disaggregated by each men\u2019s sport and each women\u2019s sport, including\u2014 (I) total expenses; and (II) each category of expenses as described in clause (ii). ; and\n**(I)**\nby adding at the end the following:\n(K) The numbers of participants who participate in 1, 2, or 3 intercollegiate sports at the institution, in the aggregate and disaggregated by each men\u2019s sport and each women\u2019s sport. (L) The total number of men that practice on women\u2019s intercollegiate teams, in the aggregate and disaggregated by each women\u2019s sport. (M) Information regarding race and ethnicity for athletes and coaches (including assistant coaches), in the aggregate and disaggregated by each men\u2019s sport and each women\u2019s sport. (N) The number of male students, and the number of female students, participating in collegiate (including intramural and club) sports at the institution. (O) A certification that the institution has verified the information submitted in the report under this paragraph. (P) With respect to the sports participation opportunities requirements under title IX of the Education Amendments of 1972\u2014 (i) a certification that the institution complies with such requirements by showing\u2014 (I) substantial proportionality; (II) a history and continuing practice of expanding sports participation opportunities; or (III) full and effective accommodation of athletics interests; and (ii) an identification of the method of compliance described in subclauses (I) through (III) of clause (i) that the institution uses. ;\n**(2)**\nin paragraph (2), by striking For the purposes of paragraph (1)(G) and inserting For the purposes of subparagraphs (G) and (H) of paragraph (1) ;\n**(3)**\nby striking paragraph (4) and inserting the following:\n(4) Submission; report; information availability (A) Institutional requirements Each institution of higher education described in paragraph (1) shall\u2014 (i) by October 15 of each year, provide the information contained in the report required under such paragraph for such year to the Secretary; and (ii) by not later than February 15 of each year, publish such information on a public Internet website of the institution in a searchable format. (B) Public availability By not later than February 15 of each year, the Secretary shall make the reports and information described in subparagraph (A) for the immediately preceding academic year available to the public, which shall include posting the reports and information on a public Internet website of the Department in a searchable format. ;\n**(4)**\nby redesignating paragraph (5) as paragraph (6);\n**(5)**\nby inserting after paragraph (4) the following:\n(5) Reports by the Secretary (A) In general By not later than 2 years after the date of enactment of the Fair Play for Women Act , and every 2 years thereafter, the Secretary shall prepare and publish a report on gender equity using the information submitted under this subsection. (B) Contents The report required under subparagraph (A) shall, in the aggregate for all institutions of higher education described in paragraph (1) and disaggregated by each individual institution\u2014 (i) identify participant gaps, if any, by indicating the number of participants that need to be added in order for participants of the underrepresented sex at the institution to match the proportion of enrolled full-time undergraduate students of the underrepresented sex at the institution; (ii) identify funding gaps, if any, by showing the percentage differences, compared to proportions of enrollment of men and women at the institution, in expenditures for athletically related student aid, recruiting, promotion, and publicity in intercollegiate athletics; and (iii) identify any trends evident in such data that address relevant inequities in intercollegiate athletics participation and financial support. ; and\n**(6)**\nin paragraph (6), as redesignated by paragraph (4)\u2014\n**(A)**\nby striking Definition .\u2014For the purposes of this subsection, the term and inserting the following:\nDefinitions .\u2014For purposes of this subsection: (A) Operating expenses The term ; and\n**(B)**\nby adding at the end the following:\n(B) Participant The term participant means an athlete in a sport who\u2014 (i) (I) is receiving the institutionally sponsored support normally provided to athletes competing at the institution involved on a regular basis during the sport\u2019s season; (II) is participating in organized practice sessions and other team meetings and activities on a regular basis during the sport\u2019s season; and (III) is listed on the eligibility or squad list maintained for the sport; or (ii) due to injury, does not meet the requirements of clause (i) but continues to receive financial aid on the basis of athletic ability in the sport. (C) Season The term season , when used with respect to an intercollegiate team sport, means the period beginning on the date of a team\u2019s first intercollegiate competitive event in an academic year and ending on the date of the team\u2019s final intercollegiate competitive event in such academic year. .\n##### (b) Elementary school and secondary school athletic programs\n**(1) In general**\nSubpart 2 of part F of title VIII of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7901 et seq. ) is amended by adding at the end the following:\n8549D. Disclosure of statistics on equality in elementary and secondary education athletic programs (a) Definitions In this section: (1) Participant The term participant means an athlete in a sport who participates in the sport in elementary school, secondary school, or interscholastic competitive events, organized practice sessions, and other team meetings and activities on a regular basis during the sport\u2019s season. (2) Season The term season , when used with respect to a team sport, means the period beginning on the date of a team\u2019s first athletic competition in an academic year and ending on the date of the team\u2019s final interscholastic athletic competition in such academic year. (3) State athletic association The term State athletic association has the meaning given the term in section 4 of the Fair Play for Women Act. (b) In general The Secretary shall collect annually, from each coeducational elementary school and secondary school that receives Federal financial assistance and has an athletic program, a report that includes the following information for the immediately preceding academic year: (1) The total number of students that attended the school, fully disaggregated and cross-tabulated by sex and race or ethnicity. (2) A listing of the school\u2019s teams that competed in athletic competition and for each such team the following data: (A) The season in which the team competed. (B) The total number of participants, fully disaggregated and cross-tabulated by sex and race or ethnicity and level of competition. (C) The total expenditures for the team from all sources, including school funds and funds provided by any other entities, such as booster organizations, including the following data: (i) The travel expenditures. (ii) The equipment expenditures (including any equipment replacement schedule). (iii) The uniform expenditures (including any uniform replacement schedule). (iv) The expenditures for facilities, including medical facilities, locker rooms, fields, and gymnasiums. (v) The total number of trainers and medical personnel, and for each trainer or medical personnel an identification of such individual\u2019s\u2014 (I) sex; and (II) employment status (including whether such individual is assigned to the team full-time or part-time, and whether such individual is a head or assistant trainer or medical services provider) and duties other than providing training or medical services. (vi) The expenditures for publicity for competitions. (vii) The total salary expenditures for coaches, including compensation, benefits, and bonuses, the total number of coaches, and for each coach an identification of such coach\u2019s\u2014 (I) sex; and (II) employment status (including whether such coach is assigned to the team full-time or part-time, and whether such coach is a head or assistant coach) and duties other than coaching. (D) The total number of competitive events (in regular and nontraditional seasons) scheduled, and for each an indication of what day of the week and time the competitive event was scheduled. (E) Whether such team participated in postseason competition, and the success of such team in any postseason competition. (c) Disclosure to students and public A school described in subsection (b) shall\u2014 (1) by October 15 of each year, make available to students, potential students, and parents of students and potential students, upon request, and to the public, the report and information required of the school under such subsection for such year; and (2) ensure that all students and parents at the school are informed of their right to request such report and information. (d) Submission; information availability On an annual basis, each school described in subsection (b) shall provide the report required under such subsection, and the information contained in such report, to the Secretary not later than 15 days after the date that the school makes such report and information available under subsection (c). (e) Duties of the Secretary The Secretary shall\u2014 (1) ensure that reports and information submitted under subsection (d) are available on the same public website, and searchable in the same manner, as the reports and information made available under section 485(g)(4)(B) of the Higher Education Act of 1965; and (2) not later than 180 days after the date of enactment of the Fair Play for Women Act \u2014 (A) notify all elementary schools, secondary schools, and State athletic associations in all States regarding the availability of the reports and information under subsection (c); and (B) issue guidance to all such elementary schools, secondary schools, and State athletic associations on how to collect and report the information required under this section. .\n**(2) Conforming amendment**\nThe table of contents in section 2 of the Elementary and Secondary Education Act of 1965 is amended by inserting after the item relating to section 8549C the following:\nSec. 8549D. Disclosure of statistics on equality in elementary and secondary education athletic programs. .\n#### 7. Training and information for athletes and employees\n##### (a) Training\n**(1) Covered local educational agency**\n**(A) Employees**\nEach covered local educational agency shall ensure that each title IX coordinator, and each employee who works with athletics or teaches physical education or health, for the covered local educational agency receives, at least once per year, training on the rights under title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ) of students at elementary schools or secondary schools, and procedures for submitting complaints of violations under title IX of the Education Amendments of 1972 to the Office for Civil Rights of the Department of Education.\n**(B) Elementary and secondary school athletes**\nEach covered local educational agency shall ensure that\u2014\n**(i)**\na title IX coordinator for the covered local educational agency provides training to athletes at elementary schools or secondary schools served by the covered local educational agency on the rights of the athletes under title IX of the Education Amendments of 1972, and procedures for submitting complaints of violations of that title to the Office for Civil Rights of the Department of Education; and\n**(ii)**\neach such athlete receives that training at least once per year.\n**(2) Covered institutions of higher education**\n**(A) Employees**\nEach covered institution of higher education shall ensure that each employee of the athletic department of the covered institution of higher education and each employee of the institution with an employment function relating to collegiate athletics receives, at least once per year, training on the rights under title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ) of students at covered institutions of higher education, and procedures for submitting complaints of violations of title IX of the Education Amendments of 1972 to the Office for Civil Rights of the Department of Education.\n**(B) Postsecondary school athletes**\nEach covered institution of higher education shall ensure that\u2014\n**(i)**\nan expert in matters relating to title IX of the Education Amendments of 1972, who is not an employee described in subparagraph (A) of the covered institution of higher education, provides training to athletes at the covered institution of higher education on the rights of the athletes under title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ), and procedures for submitting complaints of violations of that title to the Office for Civil Rights of the Department of Education; and\n**(ii)**\neach such athlete receives that training at least once per year.\n##### (b) Database\nThe Secretary of Education shall establish and maintain a database of title IX coordinators, which shall be separate from the civil rights coordinators data maintained by the Office for Civil Rights of the Department of Education. The database shall include, at a minimum, the name, phone number, and email address for each title IX coordinator. The Secretary shall make the information in the database available to the public with, and by the same means as, reports made available under section 485(g)(4)(B) of the Higher Education Act of 1965 ( 20 U.S.C. 1092(g)(4)(B) ).\n#### 8. Administrative enforcement through civil penalties\n##### (a) Noncompliance\nThe Secretary of Education shall determine, at the beginning of each year, each covered institution of higher education, covered local educational agency, elementary school, or secondary school that was found during the prior year to be in noncompliance with a requirement of section 7, or of title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ). Such administrative proceeding shall be conducted in the same manner as an administrative proceeding under section 902 of the Education Amendments of 1972 ( 20 U.S.C. 1682 ).\n##### (b) Civil penalty\nIf the Secretary of Education determines under subsection (a) that a covered institution of higher education, covered local educational agency, elementary school, or secondary school was in such noncompliance during the prior year, the Secretary may impose a civil penalty on such institution, agency, or school.\n##### (c) Further noncompliance\nIf the Secretary of Education determines under subsection (a) that a covered institution of higher education, covered local educational agency, elementary school, or secondary school was in such noncompliance during 2 or more of the prior 5 years, the Secretary shall\u2014\n**(1)**\nrequire such covered institution, covered local educational agency, elementary school, or secondary school to submit, not later than 120 days after receiving notice of the determination, a plan for coming into compliance with all requirements of section 7, and of title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ); and\n**(2)**\nmake the report publicly available.\n#### 9. Rule of construction\nNothing in this Act shall be construed to imply that intercollegiate athletic associations, State athletic associations, covered institutions of higher education, or covered local educational agencies\u2014\n**(1)**\nare not covered by title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ); or\n**(2)**\nwere not covered by that title on the day before the date of enactment of this Act.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-02-11",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1183",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fair Play for Women Act",
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
        "name": "Sports and Recreation",
        "updateDate": "2025-05-15T13:58:25Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s543is.xml"
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
      "title": "Fair Play for Women Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Play for Women Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit certain discrimination against athletes on the basis of sex by State athletic associations, intercollegiate athletic associations, and covered institutions of higher education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:02Z"
    }
  ]
}
```
